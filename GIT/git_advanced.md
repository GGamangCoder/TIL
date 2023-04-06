

# undoing

- `git restore`
작업하던 파일을 수정하다가 되돌리는 작업, 복귀되지 않음
add 하기 전(staging Area 반영 안된 상태)

- 만약 아예 새로운 파일에 대해서는 ?
`git rm - cached (file_name)`
- 이미 있던 내용(수정 사항을)을 되돌리고 싶다면, 



## git restore
```git restore <file_name>```
git이 추적하고 있던 마지막 상태(commit)로 되돌려주기


## git rm --cached <file_name>  
아직 git에 **추가되지 않은** 파일이 add 되었을 때 (staging) 되돌리기


## git restore --staged <file_name>  
git에 추가되었던 파일의 수정사항이 add 되었을 때 (staging) 되돌리기 

## git commit --amend <file_name>  
`git add` 를 진행한 파일이 있을 때, commit 메시지를 수정하고 add 된 (staging) 파일들을 직전 commit에 추가
