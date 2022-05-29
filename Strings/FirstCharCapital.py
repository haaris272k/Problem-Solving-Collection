"""You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 
For example, alison heck should be capitalised correctly as Alison Heck.
Given a full name, your task is to capitalize the name appropriately."""


a = input("Enter the name ")
lst = a.split(" ")
t = []
for i in range(len(lst)):
    b = lst[i].capitalize()
    t.append(b)
print(" ".join(t))
