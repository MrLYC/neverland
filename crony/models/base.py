# coding: utf-8

from django.utils.functional import cached_property
from django.db import models

from ycyc.base.typeutils import constants


class TaskConflictError(KeyError):
    pass


class TaskTypeNotFound(TypeError):
    pass


class TaskManager(object):
    task_mappings = {}

    @classmethod
    def register(cls, type_=None):
        def register_wrapper(model):
            type_ = type_ or model.__name__
            if type_ in cls.task_mappings:
                raise TaskConflictError(type_)
            cls.task_mappings[type_] = model
            return model
        return register_wrapper

    @classmethod
    def get_task_model(cls, type_):
        if type_ not in cls.task_mappings:
            raise TaskTypeNotFound(type_)
        return cls.task_mappings.get(type_)


TaskStatus = constants(
    enabled="enabled",
    disabled="disabled",
)


class TaskBase(models.Model):
    update_at = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=64)
    params = models.CharField(max_length=128)
    status = models.CharField(max_length=16)

    class Meta:
        abstract = True

    def is_ready(self, context):
        raise NotImplementedError()

    def make_request(self):
        return TaskRequest(
            task_type=self.type,
            task_id=self.pk,
            params=self.params,
        )

TaskRequestStatus = constants(
    pending="pending",
    working="working",
)


class TaskRequest(models.Model):
    update_at = models.DateTimeField(auto_now=True)
    activate_at = models.DateTimeField()
    task_type = models.CharField(max_length=64)
    task_id = models.IntegerField()
    status = model.CharField(max_length=16)

    @cached_property
    def task(self):
        model = TaskManager.get_task_model(self.task_type)
        return model.objects.get(pk=self.task_id)
