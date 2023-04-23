from django.db import models
#from viewflow.fields import CompositeKey
from django.contrib.auth.models import User



#ADD RELATED NAMES TO ALL FOREIGN KEYS

class User_Data(models.Model):
    """Extending users to have types, and ids"""
    ADMINISTRATION = 1
    INSTRUCTOR = 2
    STUDENT = 3

    USERS = (
        (ADMINISTRATION,'Administration'),
        (INSTRUCTOR, 'Instructor'),
        (STUDENT, 'Student')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.PositiveSmallIntegerField(choices=USERS, db_column='user_type', blank=True, null = True)
    user_id = models.IntegerField(db_column='user_id',blank=True,null=True) #blank and null for prototyping purposes

    class Meta:
        abstract = True
    

class Course(models.Model):
    course_id = models.CharField(db_column='Course_ID', primary_key=True, max_length=6)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dept_name = models.ForeignKey('Department', models.DO_NOTHING, db_column='Dept_Name', blank=True, null=True,related_name='course_dept')  # Field name made lowercase.
    credits = models.IntegerField(db_column='Credits', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.course_id

    class Meta:
        managed = False
        db_table = 'course'


class Department(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=25)  # Field name made lowercase.
    building = models.CharField(db_column='Building', max_length=10, blank=True, null=True)  # Field name made lowercase.
    budget = models.IntegerField(db_column='Budget', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'department'

class Instructor(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dept_name = models.ForeignKey(Department, models.DO_NOTHING, db_column='Dept_Name', blank=True, null=True, related_name='instructor_dept')  # Field name made lowercase.
    salary = models.IntegerField(db_column='Salary', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'instructor'


class PreReq(models.Model):
    course = models.ForeignKey(Course, models.DO_NOTHING, db_column='Course_ID', blank=True, null=True, related_name='Prereq_course')  # Field name made lowercase.
    prereq_id = models.CharField(db_column='Prereq_ID', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pre_req'


class Section(models.Model):
    course = models.ForeignKey(Course, models.DO_NOTHING, db_column='Course_ID', related_name='section_course_iD')  # Field name made lowercase.
    sec_id = models.IntegerField(db_column='Sec_ID')  # Field name made lowercase.
    semester = models.IntegerField(db_column='Semester')  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    building = models.CharField(db_column='Building', max_length=6, blank=True, null=True)  # Field name made lowercase.
    room = models.CharField(db_column='Room', max_length=3, blank=True, null=True)  # Field name made lowercase.
    capacity = models.IntegerField(db_column='Capacity', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'section'
        unique_together = (('course', 'sec_id', 'semester', 'year'),)


class Student(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=40, blank=True, null=True)  # Field name made lowercase.
    dept_name = models.ForeignKey(Department, models.DO_NOTHING, db_column='Dept_Name', blank=True, null=True, related_name='Student_department')  # Field name made lowercase.
    tot_cred = models.IntegerField(db_column='Tot_Cred', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student'


class Takes(models.Model):
    student = models.ForeignKey(Student, models.DO_NOTHING, db_column='Student_ID',related_name='takes_student_ID')  # Field name made lowercase.
    course = models.ForeignKey(Section, models.DO_NOTHING, db_column='Course_ID', related_name='takes_course_ID')  # Field name made lowercase.
    sec = models.ForeignKey(Section, models.DO_NOTHING, db_column='Sec_ID', related_name='takes_section_ID')  # Field name made lowercase.
    semester = models.ForeignKey(Section, models.DO_NOTHING, db_column='Semester',related_name='takes_semester')  # Field name made lowercase.
    year = models.ForeignKey(Section, models.DO_NOTHING, db_column='Year', related_name='takes_yeartaken')  # Field name made lowercase.
    grade = models.CharField(db_column='Grade', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'takes'
        unique_together = (('student', 'course', 'sec', 'semester', 'year'),)


class Teaches(models.Model):
    course = models.ForeignKey(Section, models.DO_NOTHING, db_column='Course_ID', related_name='teaches_courseID')  # Field name made lowercase.
    sec = models.ForeignKey(Section, models.DO_NOTHING, db_column='Sec_ID', related_name='teaches_sectionID')  # Field name made lowercase.
    semester = models.ForeignKey(Section, models.DO_NOTHING, db_column='Semester', related_name='teaches_semester')  # Field name made lowercase.
    year = models.ForeignKey(Section, models.DO_NOTHING, db_column='Year', related_name='teaches_year')  # Field name made lowercase.
    teacher = models.ForeignKey(Instructor, models.DO_NOTHING, db_column='Teacher_ID', related_name='teaches_teacher')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teaches'
        unique_together = (('course', 'sec', 'semester', 'year', 'teacher'),)

class Papers(models.Model):
    doi_id = models.CharField(db_column='DOI', primary_key=True, max_length=100)  # Field name made lowercase.
    researcher_id = models.ForeignKey(Instructor, models.DO_NOTHING, db_column='Researcher_id', blank=True, null=True)  # Field name made lowercase.
    paper_title = models.CharField(db_column='Paper_Title', max_length=100, blank=True, null=True)  # Field name made lowercase.
    publish_date = models.DateField(db_column='Publish_date', blank=True, null=True)  # Field name made lowercase.
    budget = models.IntegerField(db_column='Budget', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'papers'