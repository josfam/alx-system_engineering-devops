# Execute a command that kills another process

exec { 'killmenow':
  command => '/bin/pkill killmenow'
}

