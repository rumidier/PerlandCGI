package Metshe::Web;
use Dancer ':syntax';
use Metshe::Model;

our $VERSION = '0.1';

# ugly hack
# set db => ... occurs error with [prove] or [make test]
my $db;
sub db {
  return $db if $db;
  $db = Metshe::Model->new(
    config->{model},
  );
  $db;
}

get '/' => sub {
    template 'index';
};

get '/login' => sub {
    template 'login';
};

post '/login' => sub {
    my $row = db->single('user', { email => params->{email} });
    return 0 unless $row;
    set_cookie metshe_auth => $row->id, expires => (time() + 60 * 60 * 24 * 7 );
    return 1;
};

get '/logout' => sub {
    my $cookies = Dancer::Cookies->cookies;
    my $cookie = $cookies->{metshe_auth};
    set_cookie metshe_auth => $cookie->value, expires => (time() - 100);
    return 1;
};

get '/signup' => sub {
    template 'signup';
};

post '/signup' => sub {

  my $row = db->insert('user', {
    email    => params->{email},
    passwd   => params->{passwd},
    gender   => params->{gender},
    birthday => params->{birthday},
  });

  return 1;
};

get '/bbs/:id' => sub {
  my $id = params->{id} || 1;
  my $rows = db->search('bbs', { bbs_id => $id });
  template 'bbs', { id => $id, rows => [ $rows->all ] };
};

get '/bbs/:id/post' => sub {
  my $id = params->{id};
  send_error('Not Found', 404) unless $id;

  my $cookies = Dancer::Cookies->cookies;
  my $cookie = $cookies->{metshe_auth};
  redirect(request.uri_for('/login')) unless $cookie;

  template 'bbs_post', { id => $id };
};

post '/bbs/:id/post' => sub {
    my $id = params->{id};
    my $cookies = Dancer::Cookies->cookies;
    my $cookie = $cookies->{metshe_auth};
    send_error('Bad Request', 400) unless $cookie;
    db->insert('bbs', {
      bbs_id   => $id,
      user_id  => $cookie->value,
      comment  => params->{comment},
      reply_id => params->{reply_id} || 0,
    });
   redirect(request.uri_for("/bbs/$id"));
};

true;
