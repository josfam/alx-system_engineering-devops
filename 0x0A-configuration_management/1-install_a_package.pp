# installs flask version 2.1.0 from pip3

package {'Python':
  ensure => '3.8.10'
}

package {'Werkzeug':
  ensure => '2.1.1'
}

package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}

