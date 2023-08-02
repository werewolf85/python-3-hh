from django.test import TestCase
from .models import Worker, Comment, Resume
from django.contrib.auth.models import User

class WorkerTestCase(TestCase):
    def test_create_worker_should_success(self):
        worker = Worker.objects.create(name='John Doe', specialization='Developer', waiting_salary=50000)
        self.assertEqual(worker.name, 'John Doe')
        self.assertEqual(worker.specialization, 'Developer')
        self.assertEqual(worker.waiting_salary, 50000)

    def test_create_resume_should_success(self):
        worker = Worker.objects.create(name='John Doe', specialization='Developer', waiting_salary=50000)
        resume = Resume.objects.create(worker=worker, title='Python Developer', text='Experienced Python Developer')
        self.assertEqual(resume.worker, worker)
        self.assertEqual(resume.title, 'Python Developer')
        self.assertEqual(resume.text, 'Experienced Python Developer')

    def test_create_comment_should_success(self):
        user = User.objects.create(username='testuser')
        worker = Worker.objects.create(name='John Doe', specialization='Developer', waiting_salary=50000)
        comment = Comment.objects.create(text='Test comment', worker=worker, author=user)
        self.assertEqual(comment.text, 'Test comment')
        self.assertEqual(comment.worker, worker)
        self.assertEqual(comment.author, user)

    # def test_image_field(self):
    #     worker = Worker.objects.create(name='John Doe', specialization='Developer', waiting_salary=50000)


