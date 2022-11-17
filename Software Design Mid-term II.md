# CPSC 8700: Mid-term II

## 1. smart pointers

In modern C++ programming, the Standard Library includes smart pointers, which are used to help ensure that programs are free of memory and resource leaks and are exception-safe.
Smart pointers are used to make sure that an object is deleted if it is no longer used (referenced).

Always create smart pointers on a separate line of code, never in a parameter list, so that a subtle resource leak won't occur due to certain parameter list allocation rules.
    
Example of memory leak:
```
    void my_func()
    {
        int* valuePtr = new int(15);
        int x = 45;
        // ...
        if (x == 45)
            return;   // here we have a memory leak, valuePtr is not deleted
        // ...
        delete valuePtr;
    }
     
    int main()
    {
    }
```

Types of unique pointers:

* unique_ptr
```
A unique_ptr does not share its pointer. It cannot be copied to another unique_ptr, passed by value to a function, or used in 
any C++ Standard Library algorithm that requires copies to be made. A unique_ptr can only be moved. This means that the ownership 
of the memory resource is transferred to another unique_ptr and the original unique_ptr no longer owns it. 
```

* shared_ptr 
```
The shared_ptr type is a smart pointer in the C++ standard library that is designed for scenarios in which more than one owner 
might have to manage the lifetime of the object in memory. After you initialize a shared_ptr you can copy it, pass it by value 
in function arguments, and assign it to other shared_ptr instances. All the instances point to the same object, and share 
access to one "control block" that increments and decrements the reference count whenever a new shared_ptr is added, goes out 
of scope, or is reset. When the reference count reaches zero, the control block deletes the memory resource and itself.
```

* weak_ptr

