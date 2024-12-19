from django.db import models



class Event(models.Model):

  name = models.CharField(max_length=100)

  price_per_ticket = models.DecimalField(max_digits=10, decimal_places=2)



  def __str__(self):

    return self.name




class Booking(models.Model):

  event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)

  number_of_tickets = models.PositiveIntegerField()

  total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)



  def __str__(self):

    return f"{self.event} - {self.number_of_tickets} tickets"



class Coupon(models.Model):

  code = models.CharField(max_length=50, unique=True)

  discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)



  def __str__(self):

    return self.code







