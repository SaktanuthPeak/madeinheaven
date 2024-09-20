import mongoengine as me
import datetime

COURSE_STATUS = [
                ("pending" , "รอดำเนินการ"),
                ("active" , "เปิดใช้งาน"),
                ("disactive" , "ปิดใช้งาน")
                ]

class Course(me.Document):
    meta = {"collection":"courses"}
    name = me.StringField(max_length = 256, require = True)
    discription = me.StringField()

    professer = me.ReferenceField("User" , dbref = True)

    code = me.StringField(max_length = 32 , require = True)
    enrollment = me.IntField(min_value = 0 , max_value = 1000)
    status = me.StringField(default = "pending" , choices = COURSE_STATUS)
    creator = me.ReferenceField("User" , dbref = True)
    updater = me.ReferenceField("User" , dbref = True)
    creator_date = me.DateTimeField(required = True , default=datetime.datetime.now)
    updater_date = me.DateTimeField(required = True , default=datetime.datetime.now)



