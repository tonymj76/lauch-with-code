from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


# Create your models here.
class RefJoinMananger(models.Manager):
    def get_queryset(self):
        return super(RefJoinMananger, self).get_queryset().filter(friend__isnull=False)

class Join(models.Model):
    first_name = models.CharField("Name", max_length=129)
    email_address = models.EmailField("Email") 
    friend = models.ForeignKey("self", related_name='referral', blank=True, null=True)
    ip_address = models.GenericIPAddressField(default="1.1.1")
    ref_address = models.CharField(max_length=122, default="ABC")
    created_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    slug = models.SlugField(unique=True, allow_unicode=True)
    id_join = models.AutoField(primary_key=True)


    objects = models.Manager()
    ref_friend = RefJoinMananger()

    def get_absolute_url(self, *args, **kwargs):
        return reverse("joins_a:detail_view", kwargs={"ref_address": self.ref_address})
    
    def __str__(self):
        return self.email_address

    # def clean_email_address(self):
    #     email = self.cleaned_data['email_address']
    #     try:
    #         pass
    #     except expression as identifier:
    #         pass
    
    class Meta:
        unique_together = ("email_address", "ref_address")
        ordering = ["-created_date", "-update_date"]
#---------------------------------learning-----------------------------#
# class JoinFriends(models.Model):
#     email = models.OneToOneField(Join, related_name="Sharer")
#     friends = models.ManyToManyField(Join, related_name="Friend", blank=True)
#     email_all = models.ForeignKey(Join, related_name='emails_invite')
    
#     def __str__(self):
#         print(f"friends are {self.friends.all()}")
#         print(f" {self.email_all}")
#         print(f" {self.email}")

#         return self.friends.all()[0].email_address


def create_slug(instance, new_slug=None):
    """ a recursive function that produce slug """
    slug = slugify(instance.first_name)
    if new_slug is not None:
        slug = new_slug
    qs = Join.objects.filter(slug=slug).order_by("-id_join")
    exists = qs.exists()
    if exists:
        new_slug = f"{slug}-{qs.first().id_join}"
        return create_slug(instance, new_slug=new_slug)
    return slug


@receiver(pre_save, sender=Join)
def pre_save_slug_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

    
