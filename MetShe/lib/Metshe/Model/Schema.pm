package Metshe::Model::Schema;
use Teng::Schema::Declare;

table {
  name 'user';
  pk 'id';
  columns qw( 
    id email passwd birthday gender created_on updated_on
  );
};

table {
  name 'bbs';
  pk 'id';
  columns qw(
    id bbs_id user_id comment reply_id created_on updated_on
  );
};

1;
