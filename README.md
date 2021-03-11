# GlobalAIHubPythonCourse
![](https://github.com/mahmutAkbas/GlobalAIHubPythonCourse/blob/main/HW1.png)


```python
odd_list=list(range(1,30,2))
even_list=list(range(0,30,2))
newList=[i**2 for i in (odd_list+even_list)]
for i in newList:
  print(type(i))
```
![](https://github.com/mahmutAkbas/GlobalAIHubPythonCourse/blob/main/HW2.png)

```python
cvs = {"Cv1":{"name":"ökkeş", "surname":"baklavacı" , "birthdate":"12:7:1995" ,"how do you know programing languages":"c#,T-Sql" },
      "Cv2":{"name":"mehmet", "surname":"doğan" , "birthdate":"12:5:1995" ,"how do you know programing languages":"vb.Net,T-Sql" },
      "Cv3":{"name":"havva", "surname":"ademoğlu" , "birthdate":"12:9:1995" ,"how do you know programing languages":"python,mongodb" },
      "Cv4":{"name":"halit", "surname":"yiğitoğlu" , "birthdate":"12:10:1995" ,"how do you know programing languages":"java,oracle" },
      "Cv5":{"name":"fayza", "surname":"durak" , "birthdate":"12:12:1995" ,"how do you know programing languages":"R,matlab" }
      }
a=len(cvs)
i=1
while i<a+1:
  c="Cv"+str(i)
  print(cvs[c])
  i+=1
```
