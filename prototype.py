# Author: VintellX
# Date: 24/01/2024
# Version: 0.0.1

# Why the heck am I even doing this?

from app import recruit

class UserData:
    name: str = None
    email: str = None
    regnum: str = None
    phone: str = None
    team: str = None
    sellingpoint: str = None
    linkedin: str = None
    github: str = None
    projectolink: str = None
    resumelink: str = None
    ques1: str = None
    ques2: str = None
    ques3: str = None

    @staticmethod
    def updato(*args):
        data = {
            'name': args[0],
            'email': args[1],
            'regnum': args[2],
            'phone': args[3],
            'team': args[4],
            'sellingpoint': args[5],
            'linkedin': args[6],
            'github': args[7],
            'projectolink': args[8],
            'resumelink': args[9],
            'ques1': args[10],
            'ques2': args[11],
            'ques3': args[12]
        }
        if recruit.find_one({'email': args[1]}):
            recruit.update_one({'email': args[1]}, {'$set': data})
            return 'Updated your response!'
        recruit.insert_one(data)
        return 'Submitted your response!'
