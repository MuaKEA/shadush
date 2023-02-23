import subprocess
from copier import run_auto

def main():
    repocreate()

def repocreate(project_name, full_name= "Jacob_Hector", email = "jacob.hector@ufst.dk", repo_and_artifact_name = "Nørrebro"):
    print("Initializing git repository..")
    deleteCommand = "rm -rf desktop/tmp/pe"
    delteComRes = subprocess.run(deleteCommand, capture_output=True, shell=True)
    print(delteComRes.stdout.decode()) 
    
    directoryCreate = "mkdir desktop/tmp/pe"
    ret1 = subprocess.run(directoryCreate, capture_output=True, shell=True)
    print(ret1.stdout.decode())
    
    copyRepo = "python3 -m copier --defaults -d project_name=gitHubProjekt2023 copy git@github.ccta.dk:w33412/CreateRepo.git desktop/tmp/pe"
    print(subprocess.run(copyRepo, shell=True))


    directoryChange = "cd desktop/tmp/pe; git init -b main; git add --all; git commit -m 'hello'; git remote add origin git@github.ccta.dk:w33412/RepoTest.git; git push -u origin main;"
    ret = subprocess.run(directoryChange, capture_output=True, shell=True)
    print(ret.stdout.decode())
    subprocess.run(copyRepo, shell=True)
    
    
    subprocess.check_call(["git remote add origin https://git@github.ccta.dk:w33412/hello.git"],shell=True)
    
        
    #     subprocess.check_output(["rm", "-rf", "/desktop/tmp/pe"])
    #     run_auto('git@github.ccta.dk:w33412/CreateRepo.git', "/desktop/tmp/pe" + txt1)
    #     subprocess.call('python3 -m copier --defaults \
    #     -d project_name=CreateRepo \
    #     copy git@github.ccta.dk:devops/toolchain-springboot-ref-template.git /tmp/local_copy')
    #
    # """
    #     subprocess.run(run_auto("git@github.ceta.dk:w33412/CreateRepo.glt/desktop/tmp/pe")
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


def testCode():
    testCommnad = " cd desktop/tmp/pe; pwd"
    ret = subprocess.run(testCommnad, shell=True)
    print(ret.stdout.decode())


if __name__ == "__main__":
    #repocreate("", "", "", "")
    testCode()