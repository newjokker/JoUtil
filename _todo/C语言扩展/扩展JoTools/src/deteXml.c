#include <Python.h>
#include <stdio.h>
#include <stdint.h>
#include <string.h>

#include "str_tools/charTools.h"



static inline int __str_obj_analysis(FILE *xml_file, int count)
{
    char strTemp[1000], *fgetFlag, strGet[1000];
    int analysis_flag;
    while((fgetFlag = fgets(strTemp, 1000, xml_file)))
    {
        if((analysis_flag = str_analysis(strTemp, "name", strGet)))
        {
            printf("\tname = %s\n", strGet);
        }
        else if((analysis_flag = str_analysis(strTemp, "pose", strGet)))
        {
            printf("\tpose = %s\n", strGet);
        }
        else if((analysis_flag = str_analysis(strTemp, "truncated", strGet)))
        {
            printf("\ttruncated = %s\n", strGet);
        }
        else if((analysis_flag = str_analysis(strTemp, "difficult", strGet)))
        {
            printf("\tdifficult = %s\n", strGet);
        }
        else if((analysis_flag = str_analysis(strTemp, "xmin", strGet)))
        {
            printf("\txmin = %s\n", strGet);
        }
        else if((analysis_flag = str_analysis(strTemp, "ymin", strGet)))
        {
            printf("\tymin = %s\n", strGet);
        }
        else if((analysis_flag = str_analysis(strTemp, "xmax", strGet)))
        {
            printf("\txmax = %s\n", strGet);
        }
        else if((analysis_flag = str_analysis(strTemp, "ymax", strGet)))
        {
            printf("\tymax = %s\n", strGet);
        }
        else if(strstr(strTemp, "object"))
        {
            break;
        }
    }
    return 0;
}

int __parse_xml_as_txt(const char *xml_path)
{
    FILE *xml_file = fopen(xml_path, "r");

    if(xml_file == NULL)
    {
        return -1;
    }
    
    char strTemp[1000], *fgetFlag, strGet[1000];
    int analysis_flag, count = 0;

    while((fgetFlag = fgets(strTemp, 1000, xml_file)))
    {
        if((analysis_flag = str_analysis(strTemp, "filename", strGet)))
        {
            printf("filename = %s\n", strGet);
        }
        else if((analysis_flag = str_analysis(strTemp, "folder", strGet)))
        {
            printf("folder = %s\n", strGet);
        }
        else if((analysis_flag = str_analysis(strTemp, "height", strGet)))
        {
            printf("height = %s\n", strGet);
        }
        else if((analysis_flag = str_analysis(strTemp, "width", strGet)))
        {
            printf("width = %s\n", strGet);
        }
        else if((analysis_flag = str_analysis(strTemp, "depth", strGet)))
        {
            printf("depth = %s\n", strGet);
        }
        else if((analysis_flag = str_analysis(strTemp, "path", strGet)))
        {
            printf("path = %s\n", strGet);
        }
        else if((analysis_flag = str_analysis(strTemp, "segmented", strGet)))
        {
            printf("segmented = %s\n", strGet);
        }
        // else if((analysis_flag = str_analysis(strTemp, "source", strGet)))
        // {
        //     printf("source = %s\n", strGet);
        // }
        else if(strstr(strTemp, "object"))
        {
            printf("object%d\n",++count);
            __str_obj_analysis(xml_file, count);
        }
    }

    return 0;
}

PyObject *str_obj_analysis(FILE *xml_file)
{
    PyObject *res = PyDict_New();
    PyObject *bndbox = PyDict_New();
    PyDict_SetItemString(res, "bndbox", bndbox);
    
    char strTemp[1000], *fgetFlag, strGet[1000];
    int analysis_flag;
    PyObject *value;
    while((fgetFlag = fgets(strTemp, 1000, xml_file)))
    {
        if((analysis_flag = str_analysis(strTemp, "name", strGet)))
        {
            value = PyUnicode_FromStringAndSize(strGet, strlen(strGet));
            PyDict_SetItemString(res, "name", value);\
            Py_DECREF(value);
        }
        else if((analysis_flag = str_analysis(strTemp, "prob", strGet)))
        {
            value = PyLong_FromLong(atoi(strGet));
            PyDict_SetItemString(res, "prob", value);
            Py_DECREF(value);
        }
        else if((analysis_flag = str_analysis(strTemp, "id", strGet)))
        {
            value = PyLong_FromLong(atoi(strGet));
            PyDict_SetItemString(res, "id", value);
            Py_DECREF(value);
        }
        else if((analysis_flag = str_analysis(strTemp, "des", strGet)))
        {
            value = PyUnicode_FromStringAndSize(strGet, strlen(strGet));
            PyDict_SetItemString(res, "des", value);
            Py_DECREF(value);
        }
        else if((analysis_flag = str_analysis(strTemp, "crop_path", strGet)))
        {
            value = PyUnicode_FromStringAndSize(strGet, strlen(strGet));
            PyDict_SetItemString(res, "crop_path", value);
            Py_DECREF(value);
        }
        else if((analysis_flag = str_analysis(strTemp, "xmin", strGet)))
        {
            value = PyLong_FromLong(atoi(strGet));
            PyDict_SetItemString(bndbox, "xmin", value);
            Py_DECREF(value);
        }
        else if((analysis_flag = str_analysis(strTemp, "ymin", strGet)))
        {
            value = PyLong_FromLong(atoi(strGet));
            PyDict_SetItemString(bndbox, "ymin", value);
            Py_DECREF(value);
        }
        else if((analysis_flag = str_analysis(strTemp, "xmax", strGet)))
        {
            value = PyLong_FromLong(atoi(strGet));
            PyDict_SetItemString(bndbox, "xmax", value);
            Py_DECREF(value);
        }
        else if((analysis_flag = str_analysis(strTemp, "ymax", strGet)))
        {
            value = PyLong_FromLong(atoi(strGet));
            PyDict_SetItemString(bndbox, "ymax", value);
            Py_DECREF(value);
        }
        else if(strstr(strTemp, "object"))
        {
            break;
        }
    }
    return res;
}

static PyObject *parse_xml_as_txt(PyObject *self, PyObject *args)
{
    char *xml_path;
    if(!PyArg_ParseTuple(args, "s", &xml_path))
    {
        Py_RETURN_NONE;
    }
    
    FILE *xml_file = fopen(xml_path, "r");
    if(xml_file == NULL)
    {
        printf("cannot open file %s\n", xml_path);
        Py_RETURN_NONE;
    }

    char strTemp[1000], *fgetFlag, strGet[1000];
    int analysis_flag;

    PyObject *res = PyDict_New();
    PyObject *size_temp = PyDict_New();
    PyObject *list_temp = PyList_New(0);

    PyDict_SetItemString(res, "size", size_temp);
    PyDict_SetItemString(res, "object", list_temp);

    PyObject *value;

    while((fgetFlag = fgets(strTemp, 1000, xml_file)))
    {
        if((analysis_flag = str_analysis(strTemp, "filename", strGet)))
        {
            value = PyUnicode_FromStringAndSize(strGet, strlen(strGet));
            PyDict_SetItemString(res, "filename", value);
            Py_DECREF(value);
        }
        else if((analysis_flag = str_analysis(strTemp, "folder", strGet)))
        {
            value = PyUnicode_FromStringAndSize(strGet, strlen(strGet));
            PyDict_SetItemString(res, "folder", value);
            Py_DECREF(value);
        }
        else if((analysis_flag = str_analysis(strTemp, "height", strGet)))
        {
            value = PyLong_FromLong(atoi(strGet));
            PyDict_SetItemString(size_temp, "height", value);
            Py_DECREF(value);
        }
        else if((analysis_flag = str_analysis(strTemp, "width", strGet)))
        {
            value = PyLong_FromLong(atoi(strGet));
            PyDict_SetItemString(size_temp, "width", value);
            Py_DECREF(value);
        }
        else if((analysis_flag = str_analysis(strTemp, "depth", strGet)))
        {
            value = PyLong_FromLong(atoi(strGet));
            PyDict_SetItemString(size_temp, "depth", value);
            Py_DECREF(value);
        }
        else if((analysis_flag = str_analysis(strTemp, "path", strGet)))
        {
            value = PyUnicode_FromStringAndSize(strGet, strlen(strGet));
            PyDict_SetItemString(res, "path", value);
            Py_DECREF(value);
        }
        else if((analysis_flag = str_analysis(strTemp, "segmented", strGet)))
        {
            value = PyUnicode_FromStringAndSize(strGet, strlen(strGet));
            PyDict_SetItemString(res, "segmented", value);
            Py_DECREF(value);
        }
        else if((analysis_flag = str_analysis(strTemp, "source", strGet)))
        {
            value = PyUnicode_FromStringAndSize(strGet, strlen(strGet));
            PyDict_SetItemString(res, "source", value);
            Py_DECREF(value);
        }
        else if(strstr(strTemp, "object"))
        {
            value = str_obj_analysis(xml_file);
            PyList_Append(list_temp, value);
        }
    }

    Py_DECREF(size_temp);
    Py_DECREF(list_temp);
    fclose(xml_file);
    return res;
}


static PyObject *add(PyObject* self, PyObject* args, PyObject* keyds)
{
    static char* kwlist[] = {"age","name","level",NULL};
    int age;
    char *name;
    int level;
    if(!PyArg_ParseTupleAndKeywords(args,keyds,"isi", kwlist, &age,&name,&level))
    {
        return NULL;
    }
    /* 其他的工作 */
	return PyLong_FromLong(age + level);
}

static PyObject *test(PyObject* self, PyObject* args)
{
    int age;
    char *name;
    int level;
    if(!PyArg_ParseTuple(args, "isi", &age, &name, &level))
    {
        return NULL;
    }
    /* 其他的工作 */
	return PyLong_FromLong(age + level);
}

static PyObject *test_002(PyObject* self, PyObject* args, PyObject* kwargs)
{
    static char* kwlist[] = {"age","name","level",NULL};
    int age;
    char *name;
    int level;
    if(!PyArg_ParseTupleAndKeywords(args,kwargs,"isi", kwlist, &age,&name,&level))
    {
        return NULL;
    }
    /* 其他的工作 */
	return PyLong_FromLong(age + level);
}



static PyMethodDef XmlReadMethods[] = {
    {"parse_xml_as_txt", parse_xml_as_txt, METH_VARARGS, "read xml like txt"},
	{"add", add, METH_VARARGS, "test"},
	{"test", test, METH_VARARGS, "test"},
	{"test_002", test_002, METH_VARARGS | METH_KEYWORDS, "test"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef deteXmlmodule = {
    PyModuleDef_HEAD_INIT,
    "deteXml",
    "xml read by using c/c++",
    -1,
    XmlReadMethods
};

PyMODINIT_FUNC PyInit_deteXml(void)
{
    return PyModule_Create(&deteXmlmodule);
}


int main(int argc, char **argv)
{
    wchar_t *program = Py_DecodeLocale(argv[0], NULL);
    if (program == NULL) {
        fprintf(stderr, "Fatal error: cannot decode argv[0]\n");
        exit(1);
    }

    /* Add a built-in module, before Py_Initialize */
    PyImport_AppendInittab("deteXml", PyInit_deteXml);

    /* Pass argv[0] to the Python interpreter */
    Py_SetProgramName(program);

    /* Initialize the Python interpreter.  Required. */
    Py_Initialize();

    /* Optionally import the module; alternatively,
       import can be deferred until the embedded script
       imports it. */
    PyImport_ImportModule("deteXml");

    PyMem_RawFree(program);

    return 0;
}
