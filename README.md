# Implementing a Buffer Pool Manager prototype in Python

Inspired from CMU 15-445/645: http://15445.courses.cs.cmu.edu/fall2017/project1/

Submitted as programming project for Database Management Systems course 
at BML Munjal University to Dr. Brij Bihari Dubey and Dr. Rajesh Yadav.

## Structure of Code

* page.py
    * Consists of a 'kinda' stub implementation of a page with necessary functions.
    * A page consists of an index, a randomly generated UUID, a state variable
        ('REFERENCED', 'AVAILABLE' or 'PINNED'), and a boolean to check if the page
        is 'dirty' (Changed in memory), pin count.
    * Methods to increment and decrement number of pins, to get pin count and to check
        if the page is dirty.
        
* disk_manager.py
    * STUB implemetations of all methods needed in a Disk Manager to implement a buffer
        pool manager. Nothing to see there.
        
* replacer.py
    * Abstract class with all methods a valid replacement policy must implement. These
        methods are: 'insert', 'victim', 'replace', 'length'
        
* lru_replacer.py
    * Implementaion of Least Recently Used (LRU) replacement policy.
    * Uses a circular queue to find the least recently used page.
    
* buffer_manager.py
    * Real FUN is here !!!
    * Methods to create, fetch, delete, pin / unpin pages.