from django.test import TestCase

from blog.forms import NewCommentForm

class NewCommentFormTest(TestCase):
    def test_new_comment_form_comment_help_text(self):
        form = NewCommentForm()
        self.assertEqual(form.fields['comment'].help_text, 'Enter a comment about blog post here.')
    
    def test_new_comment_form_max_ok(self):
        sample_comment="hello"
        form = NewCommentForm(data={'comment':sample_comment})
        self.assertTrue(form.is_valid())

    def test_new_comment_form_max_over(self):
        sample_comment = "hello"*1000
        form = NewCommentForm(data={'comment':sample_comment})
        self.assertTrue(form.is_valid())
