# installs flask version 2.1.0 from pip3

package { 'pip3':
  provider  => 'pip3'
}

package { 'Werkzeug':
  ensure => '2.1.1'
}

package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => [
    Package['pip3'],
    Package['Werkzeug']
  ]
}

