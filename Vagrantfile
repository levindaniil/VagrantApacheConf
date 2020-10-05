Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.provision :shell, path: "bootstrap.sh"  
  config.vm.network "forwarded_port", guest: 80, host: 80
  config.vm.network "forwarded_port", guest: 443, host: 443
  
  
  config.hostmanager.enabled = true
  config.hostmanager.manage_host = true
  config.hostmanager.aliases = %w(python.com html.com)
end