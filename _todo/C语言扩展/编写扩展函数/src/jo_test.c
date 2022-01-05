#include <Python.h>
#include <stdio.h>
#include <stdint.h>
#include <string.h>






static PyObject *test_001(PyObject* self, PyObject* args, PyObject* kwargs)
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
    //{"parse_xml_as_txt", parse_xml_as_txt, METH_VARARGS, "read xml like txt"},
	//{"add", add, METH_VARARGS, "test"},
	//{"test", test, METH_VARARGS, "test"},
	{"test_001", test_001, METH_VARARGS | METH_KEYWORDS, "test_001"},
    {NULL, NULL, 0, NULL}
};


// --------------------------------------------------------------------------------------------------


static struct PyModuleDef deteXmlmodule = {
    PyModuleDef_HEAD_INIT,
    "jo_test",
    "xml read by using c/c++",
    -1,
    XmlReadMethods
};

PyMODINIT_FUNC PyInit_jo_test(void)
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
    PyImport_AppendInittab("jo_test", PyInit_jo_test);

    /* Pass argv[0] to the Python interpreter */
    Py_SetProgramName(program);

    /* Initialize the Python interpreter.  Required. */
    Py_Initialize();

    /* Optionally import the module; alternatively,
       import can be deferred until the embedded script
       imports it. */
    PyImport_ImportModule("jo_test");

    PyMem_RawFree(program);

    return 0;
}
