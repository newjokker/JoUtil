#include "charTools.h"
#include <string.h>

inline int str_analysis(const char *strTemp, const char *xml_flag, char *strGet)
{
    char *xmlFlag1, *xmlFlag2;
    int xml_len;

    if((xmlFlag1 = strstr(strTemp, xml_flag)))
    {
        xmlFlag1 += strlen(xml_flag) + 1;
        if((xmlFlag2 = strstr(xmlFlag1, xml_flag)))
        {
            xmlFlag2 -= 2;
            xml_len = xmlFlag2 - xmlFlag1;
            strncpy(strGet, xmlFlag1, xml_len);
            strGet[xml_len] = '\0';
        }
        else
        {
            strGet[0] = '\0';
        }
        return 1;
    }
    return 0;
}