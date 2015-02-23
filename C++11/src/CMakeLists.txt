ADD_EXECUTABLE ( bfs_main 
    main.cc    
    light_queue.h
    bfs.h
)

INSTALL (TARGETS bfs_main DESTINATION bin)
