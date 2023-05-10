# Fix server error when Apache web server receives GET request via HTTP

exec {'replace':
  provide => shell,
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
