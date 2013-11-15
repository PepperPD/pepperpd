PREREQS_MD5_DIR = ENV["PREREQ_CACHE_DIR"] || File.join(REPO_ROOT, '.prereqs_cache')

CLOBBER.include(PREREQS_MD5_DIR)

directory PREREQS_MD5_DIR

desc "Install all prerequisites needed for the lms and cms"
task :install_prereqs => [:install_node_prereqs, :install_ruby_prereqs]

desc "Install all node prerequisites for the lms and cms"
task :install_node_prereqs => "ws:migrate" do
    unchanged = 'Node requirements unchanged, nothing to install'
    when_changed(unchanged, ['package.json']) do
        sh('npm install')
    end unless ENV['NO_PREREQ_INSTALL']
end

desc "Install all ruby prerequisites for the lms and cms"
task :install_ruby_prereqs => "ws:migrate" do
    unchanged = 'Ruby requirements unchanged, nothing to install'
    when_changed(unchanged, ['Gemfile']) do
        sh('bundle install')
    end unless ENV['NO_PREREQ_INSTALL']
end
