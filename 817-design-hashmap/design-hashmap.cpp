class MyHashMap {
public:
    MyHashMap() {
    }

    unordered_map<int, int> myhashmap;
    
    void put(int key, int value) {
        if(myhashmap.contains(key)) {
            myhashmap.erase(key);
            myhashmap.insert({key, value});
        } else {
            myhashmap.insert({key, value});
        }
    }
    
    int get(int key) {
        if(myhashmap.contains(key)) return myhashmap[key];
        else return -1;
    }
    
    void remove(int key) {
        myhashmap.erase(key);
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */