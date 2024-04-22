# sets up an ssh configuration file
file {'/etc/ssh/ssh_config':
  ensure  => 'present',
  content => "IdentityFile ~/.ssh/school\n
              PasswordAuthentication no\n",
}

