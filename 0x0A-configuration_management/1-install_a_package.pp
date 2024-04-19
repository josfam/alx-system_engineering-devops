# installs flask version 2.1.0 from pip3

package {'pip3':
  ensure   => 'installed',
  provider => 'pip3'
}

package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}

