import subprocess

from copier import run_auto


class MainClass:

    def repocreate(project_name, full_name= "Jacob_Hector", email = "jacob.hector@ufst.dk", repo_and_artifact_name = "Nørrebro"):

        deleteCommand = "rm -rf desktop/tmp/pe"
        delteComRes = subprocess.run(deleteCommand, capture_output=True, shell=True)
        print(delteComRes.stdout.decode())
        txt1 = ["python3 -m copier --defaults -d project_name=gitHubProjekt2023 copy git@github.ccta.dk:w33412/CreateRepo.git desktop/tmp/pe"]
        print(subprocess.run(txt1, shell=True))

        command = "cd /desktop/tmp/pe; git init -b main; git add --all; git commit -m 'hello'; git remote add origin git@github.ccta.dk:w33412/RepoTest.git; git push -u origin main; git push;"
        ret = subprocess.run(command, capture_output=True, shell=True)
        print(ret.stdout.decode())


    #     print("Initializing git repository..")
    #     subprocess.check_output(["rm", "-rf", "/desktop/tmp/pe"])
    #     run_auto('git@github.ccta.dk:w33412/CreateRepo.git', "/desktop/tmp/pe" + txt1)
    #     subprocess.call('python3 -m copier --defaults \
    #     -d project_name=CreateRepo \
    #   copy git@github.ccta.dk:devops/toolchain-springboot-ref-template.git /tmp/local_copy')
    #
    # """
    #     subprocess.run(run_auto("eit@eithub.ceta.dk:433412/CreateRepo.glt/desktop/tmp/pe")
    #     subprocess.call(python3 -m copier --defaults \
    #     -d project_name="<CreateRepo>" \
    #     copy git@github.ccta.dk:devops/toolchain-springboot-ref-template.git /tmp/local_copy
    #     copy eit@github.ceta.dk devops/toolchain-springboot-ref-template.git/trp/local_copy’)
    #    """
    # #subprocess.call(["cd", "/desktop/tmp/pe"],shell=True)
    # #subprocess.check_call(["git remote add origin https://git@github.ccta.dk:w33412/hello.git"],shell=True)
    # # subprocess.check_call(["git  push -u origin main"],shell=True)
    #

    # subprocess.check_call([ copier copy -d git@github.ccta.dk: devops/toolchain-springboot-ref-template.git/tmp/pe, shell-t \])
    # subprocess.check_call([ copier copy -d project_name="githubProjekt2023" \])
    # subprocess.check_call([ copier copy -d repo. and artifact name-"githubProjekt2023githubProjekt2023" \])
    # subprocess.check call([ copier copy -d email="projektet@ufst.dk" \])
    # subprocess.check_call([ copier copy -d full name-"Jacob Hector" 11)
    # subprocess.check_call([ copier copy -d git remote add origin "https://git@github.ccta.dk:kvalitet-og-test/devops-spring-boot-ref.git" \])
    # subprocess.check_call([ copier copy -d . run auto ("git@github.ccta.dk:w33412/create-repo-test-clone.git" )],
    #                       subprocess. Popen ("1s", CWd = "/devops-springboot-ref")

    if __name__ == '__main__':
        repocreate("sucuk", "", "", "")
