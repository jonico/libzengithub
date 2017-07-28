def artifactory_name = "artifactory"
def artifactory_repo = "conan"
def repo_url = 'https://github.com/jonico/libzengithub.git'
def repo_branch = "master"

node {
    stage("Get recipe"){
        git branch: repo_branch, url: repo_url
    }

    stage("Configure Artifactory/Conan")
      def server = Artifactory.server artifactory_name
      def client = Artifactory.newConanClient()
      def serverName = client.remote.add server: server, repo: artifactory_repo
      client.run(command: "remote remove conan.io")

    stage("Test recipe"){
        client.run(command: "test_package")
    }

    stage("Upload packages"){
        String command = "upload * --all -r ${serverName} --confirm"
        def b = client.run(command: command)
        server.publishBuildInfo b
    }
}
