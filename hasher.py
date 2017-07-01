import hashlib
from random import randint

class HashCracker:
    """
    A class aimed at understanding the probability and statistics behind mining processes, for block chain addition
    """
    def __init__(self, data=None, expexted_hash=None, append=None, debug = False, append_at = 'back'):
        """
        
        :param str data: The string which needs to be hashed 
        :param str expexted_hash: The beginning part of the digest as required 
        :param str append: The object to append at end of the string input 
        :param bool debug: The parameter which says if debug info should be shown
        :param str append_at: The parameter which decides if we need to append at back or front
        """
        self._data = data
        self._expected_hash = expexted_hash
        self._append = append
        self._debug = debug
        self._append_at = append_at

    def _mine(self):
        """
        The function which generates the hash and compares with the expected hash
        :return:
        """
        hash_machine = hashlib.sha256(self._data.encode())
        digest = str(hash_machine.hexdigest( ))
        score = 0
        for i in range(0,len(self._expected_hash)):
            if digest[i] == self._expected_hash[i]:
                score = score + 1
        match_percent = (score/len(self._expected_hash))*100
        if self._debug is True or match_percent is 100:
            print('{} matches expected by {} %'.format(digest,match_percent))
        return match_percent

    def simple_miner(self):
        """
        The simplest miner to mine and display stats on console
        :return:
        """
        counter = 0
        while self._mine() != 100:
            counter = counter + 1
            if self._append is 'random':
                if self._append_at is 'back':
                    self._data = self._data + str(randint(0,9))
                else:
                    self._data = str(randint(0,9)) + self._data
            else:
                if self._append_at is 'back':
                    self._data = self._data + self._append
                else:
                    self._data = self._append + self._data
            if self._debug is True or self._mine() is 100:
                print('{}th try - {}'.format(counter, self._data))


if __name__ == '__main__':
    node = HashCracker(data='samvram', expexted_hash='0', append='random', debug=True, append_at='back')
    node.simple_miner()