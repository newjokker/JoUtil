
package main

import (
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"io"
	"os"
	"time"
	"jogo"
)

func getFileMd5(file_path string) string {
	pFile, err := os.Open(file_path)
	if err != nil {
		fmt.Errorf("open file failed，filename=%v, err=%v", file_path, err)
		return ""
	}
	defer pFile.Close()
	md5h := md5.New()
	io.Copy(md5h, pFile)
	return hex.EncodeToString(md5h.Sum(nil))
}

func main() {

    function.Test()

    var file_list []string

	start_time := time.Now()
	fileName := "/home/ldq/golang/img/87285e857438e3c3540477118ec09d1f.jpg"
	file_dir := "/home/ldq/golang/img"

	file_list, _ = function.GetAllFile(file_dir, file_list)

    fmt.Println("len file_list : ", len(file_list))


	md5Val := getFileMd5(fileName)
	fmt.Println("配置文件的md5值", md5Val)
	elapsed_time := time.Since(start_time)
    fmt.Println("fun use time : ", elapsed_time)
}
