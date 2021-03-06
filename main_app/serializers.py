from rest_framework import serializers
from .models import *


# api/lk
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'middle_name', 'last_name', 'email', 'school', 'date_of_birth')


# api/tasks/id
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Test
        fields = ('id', 'question', 'answer', 'is_visible')


class CurrentTaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = TaskDetail
        fields = ('id', 'is_done', 'last_code')


class CurrentTaskSerializer(serializers.ModelSerializer):
    task_detail = CurrentTaskDetailSerializer(read_only=True, many=True)
    tests = TestSerializer(read_only=True, many=True)

    class Meta:
        depth = 2
        model = Task
        fields = ('id', 'name', 'theory', 'mission', 'task_detail', 'languages', 'tests')


# api/blocks/id/new_task - creating new task
class ChangeBlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'name')


# api/blocks/id/new_task - creating new task
class CreateChangeTaskSerializer(serializers.ModelSerializer):
    test = TestSerializer(read_only=True, many=True)

    class Meta:
        depth = 2
        model = Task
        fields = ('id', 'name', 'theory', 'mission', 'sprint', 'test')


# api/classes/id/new_block - creating new sprint
class CreateSprintSerializer(serializers.ModelSerializer):

    class Meta:
        depth = 2
        model = Sprint
        fields = ('id', 'name', 'grade')


# api/my_classes
class MyCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Grade
        fields = ('id', 'name')


# api/classes/id
class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = TaskDetail
        fields = ('id', 'is_done', 'last_code')


class TaskSerializer(serializers.ModelSerializer):
    task_detail = TaskDetailSerializer(read_only=True, many=True)

    class Meta:
        depth = 2
        model = Task
        fields = ('id', 'name', 'task_detail')


class SprintSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        depth = 2
        model = Sprint
        fields = ('id', 'name', 'tasks')


class GradeSerializer(serializers.ModelSerializer):
    sprints = SprintSerializer(many=True, read_only=True)

    class Meta:
        depth = 2
        model = Grade
        fields = ('id', 'name', 'sprints')
