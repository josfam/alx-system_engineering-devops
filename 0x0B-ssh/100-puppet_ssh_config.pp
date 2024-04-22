# sets up an ssh configuration file
file {'~/.ssh/school':
  ensure  => 'present',
  content => "IdentityFile ~/.ssh/school\n
              PasswordAuthentication no\n",
}

