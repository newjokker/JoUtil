package function

import (
        "fmt"
        "io/ioutil"
        "path"
        "C"
)

func GetAllFile(pathname string, s []string) ([]string, error) {
        rd, err := ioutil.ReadDir(pathname)
        if err != nil {
                fmt.Println("read dir fail:", err)
                return s, err
        }
        for _, fi := range rd {
                if fi.IsDir() {
                        fullDir := pathname + "/" + fi.Name()
                        s, err = GetAllFile(fullDir, s)
                        if err != nil {
                                fmt.Println("read dir fail:", err)
                                return s, err
                        }
                } else {
                        fullName := pathname + "/" + fi.Name()
                        s = append(s, fullName)
                }
        }
        return s, nil
}

func AnalysisFile(s []string){
    // map for store suffix numb
    var SuffixMap map[string]int
    SuffixMap = make(map[string]int)
    // analysis file suffix
    for i, n := 0, len(s); i < n; i++ {
        filename :=  s[i]
        filesuffix := path.Ext(filename)
        suffix_num, ok := SuffixMap[filesuffix]
        if(ok) {
            SuffixMap[filesuffix] = suffix_num + 1
        } else {
            SuffixMap[filesuffix] = 1
        }
    }
    // print analysis result
    var file_sum int
    file_sum = 0
    for k, v := range SuffixMap {
        file_sum += v
        fmt.Printf("%-20s %d\n", k, v)
        fmt.Printf("---------------------------\n")}
    fmt.Printf("%-20s %d\n", "file_numb_sum", file_sum)
}

// func main() {
//         var s []string
//         // flag
//         var analysis_dir = flag.String("ad", "./", "string类型参数")
//         flag.Parse()
//         // input
//         // fmt.Println("input analysis dir : ")
//         // fmt.Scanln(&analysis_dir)
//         start_time := time.Now()
//         s, _ = GetAllFile(*analysis_dir, s)
//         AnalysisFile(s)
//         // get execute time
//         elapsed_time := time.Since(start_time)
//         fmt.Println("fun use time : ", elapsed_time)
// }
