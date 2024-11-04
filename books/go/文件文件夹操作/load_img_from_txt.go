package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strings"
    "net/http"
	"io/ioutil"
	"time"
    "flag"
)

func DownLoadImg(save_dir string, url string) error {
    save_path := save_dir
    idx := strings.LastIndex(url, "/")
    if idx < 0 {
        save_path += url
    } else {
        save_path += url[idx:]
    }
    v, err := http.Get(url)
    if err != nil {
        fmt.Printf("Http get [%v] failed! %v", url, err)
        return err
    }
    defer v.Body.Close()
    content, err := ioutil.ReadAll(v.Body)
    if err != nil {
        fmt.Printf("Read http response failed! %v", err)
        return err
    }
    err = ioutil.WriteFile(save_path, content, 0666)
    if err != nil {
        fmt.Printf("Save to file failed! %v", err)
        return err
    }
    return nil
}

func main() {

    var i int
    var txt_path = flag.String("txt_path", "./test.txt", "string")
    var save_dir = flag.String("save_dir", "./", "string")
    flag.Parse()

    start_time := time.Now()

    // open txt file
	file, err := os.Open(*txt_path)
	if err != nil {
		fmt.Println("open txt filed : ", err)
		os.Exit(3)
	}
	defer file.Close()

	br := bufio.NewReader(file)
    for {
        url, _, c := br.ReadLine()
        if c == io.EOF {
            break
        }
        i ++
        fmt.Printf("%d : %s\n", i, string(url))
        DownLoadImg(*save_dir, string(url))
    }

    elapsed_time := time.Since(start_time)
    fmt.Println("fun use time : ", elapsed_time)
}
