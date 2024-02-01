# Install apache2
class {'apache2':
  mpm_module => 'prefork',
  require    => Package['apache2'],
}

# Enable required Apache modules
apache2::mod { ['rewrite', 'ssl', 'headers']:
  ensure => 'present',
}

# Define the web_static module
class web_static {
  # Create web_static directories
  file { '/data':
    ensure => 'directory',
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  file { '/data/web_static':
    ensure => 'directory',
    owner  => 'root',
    group  => 'root',
  }

  file { '/data/web_static/releases':
    ensure => 'directory',
    owner  => 'root',
    group  => 'root',
  }

  file { '/data/web_static/shared':
    ensure => 'directory',
    owner  => 'root',
    group  => 'root',
  }

  file { '/data/web_static/current':
    ensure => 'link',
    target => '/data/web_static/releases/test',
    owner  => 'root',
    group  => 'root',
  }

  # Create index.html file
  file { '/data/web_static/releases/test/index.html':
    ensure  => 'file',
    owner   => 'root',
    group   => 'root',
    content => '<html><head></head><body>Holberton School</body></html>',
  }
}

# Apply the web_static class
include web_static
