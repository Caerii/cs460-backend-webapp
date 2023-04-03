from django.db import models

class Course(models.Model): #Course table
    course_id = models.CharField(db_column='Course_ID', primary_key=True, max_length=6)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dept_name = models.ForeignKey('Department', models.DO_NOTHING, db_column='Dept_Name', blank=True, null=True)  # Field name made lowercase.
    credits = models.IntegerField(db_column='Credits', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'course'


class Department(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=25)  # Field name made lowercase.
    building = models.CharField(db_column='Building', max_length=10, blank=True, null=True)  # Field name made lowercase.
    budget = models.IntegerField(db_column='Budget', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'department'

class Instructor(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dept_name = models.ForeignKey(Department, models.DO_NOTHING, db_column='Dept_Name', blank=True, null=True)  # Field name made lowercase.
    salary = models.IntegerField(db_column='Salary', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'instructor'


class PreReq(models.Model):
    course = models.ForeignKey(Course, models.DO_NOTHING, db_column='Course_ID', blank=True, null=True)  # Field name made lowercase.
    prereq_id = models.CharField(db_column='Prereq_ID', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pre_req'


class Section(models.Model):
    course = models.ForeignKey(Course, models.DO_NOTHING, db_column='Course_ID')  # Field name made lowercase.
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
    dept_name = models.ForeignKey(Department, models.DO_NOTHING, db_column='Dept_Name', blank=True, null=True)  # Field name made lowercase.
    tot_cred = models.IntegerField(db_column='Tot_Cred', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student'


class Takes(models.Model):
    student = models.ForeignKey(Student, models.DO_NOTHING, db_column='Student_ID')  # Field name made lowercase.
    course = models.ForeignKey(Section, models.DO_NOTHING, db_column='Course_ID')  # Field name made lowercase.
    sec_id = models.ForeignKey(Section, models.DO_NOTHING, db_column='Sec_ID')  # Field name made lowercase.
    semester = models.ForeignKey(Section, models.DO_NOTHING, db_column='Semester')  # Field name made lowercase.
    year = models.ForeignKey(Section, models.DO_NOTHING, db_column='Year')  # Field name made lowercase.
    grade = models.CharField(db_column='Grade', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'takes'
        unique_together = (('student', 'course', 'sec', 'semester', 'year'),)


class Teaches(models.Model):
    course = models.ForeignKey(Section, models.DO_NOTHING, db_column='Course_ID')  # Field name made lowercase.
    sec_id = models.ForeignKey(Section, models.DO_NOTHING, db_column='Sec_ID')  # Field name made lowercase.
    semester = models.ForeignKey(Section, models.DO_NOTHING, db_column='Semester')  # Field name made lowercase.
    year = models.ForeignKey(Section, models.DO_NOTHING, db_column='Year')  # Field name made lowercase.
    teacher = models.ForeignKey(Instructor, models.DO_NOTHING, db_column='Teacher_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teaches'
        unique_together = (('course', 'sec', 'semester', 'year', 'teacher'),)