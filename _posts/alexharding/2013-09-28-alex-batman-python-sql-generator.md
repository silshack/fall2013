---
layout: post
author: alexharding
published: true
---

Hey all - So I decided to try and do something this weekend and push myself to see if some of the things I've been learning through SILS are clicking with me enough to attempt a project of my own design.


## Project Purpose
As an avid comics reader, I've been collecting Batman comics since the "new 52" reboot in 2011 (more info [here](http://en.wikipedia.org/wiki/The_New_52), essentially a reboot of all titles to start with #1 again), and I wanted to both catalogue my existing collection and also have some way of generating what I don't currently own and want to look for, or give to family as gift ideas come holiday season.

I figured I could probably accomplish most of that with excel or access, but I decided instead to try and make myself a database so I can get some extra SQL practice and generate queries that way. I came up with a relatively simple schema, with a table for issues collecting some basic information about issues, and a table for ownership that refers to it.

The thing about comics is that although a single issue is published each month, a number of prints and variants are printed per title. Outside of promotional titles and some exceptional months, there's a pattern to how a monthly title is published. Typically there are four versions of each title published per month. One normal cover, one "variant" where the cover is drawn by a guest artist (usually with a 1:25 rarity), one variant with a non-colored cover (the same cover as normal, but the sketch originally done by the artist before it's been inked and colored, with a 1:100 rarity) and a digital combo pack with a slightly different colored title and including a digital combo code.

For my purposes, the only comics I wanted to track are normal covers, guest variants and sketch variants. Often issues sell out, and DC publishes a second print of the normal cover, usually tinted red. I decided to track those as well.

##How does this relate to Python?
So, given the 23 issues currently published, with four trackable titles per issue, that's 92 SQL insert statements I'd have to write, which sounded like a real pain. I decided to try and use what we've learned so far through class (and with some supplementary teaching by running through tutorials on code academy in my spare time) and write a python script that would generate these SQL insert statements for me. 

What made me realize this was a distinct possibility was one favor that DC did for me... on the UPC of every comic, DC includes a 5 digit number who's digits correspond to certain metadata about the comic. For example, a comic with the code 01131 is issue number 11, cover number 3, printing number 1. The first three digits signify the issue number, the fourth the cover (with '2' for guest variant and '3' for sketch cover), and the last what printing it is. To me, that meshed perfectly with what we've learned about string slicing, and I reverse-engineered the problem from there.

##My code

I realized that given an input list of '001' to '023', I could make a number generator that creates the 5 digit codes for each issue, assuming each issue has a normal cover, a second printing, a guest variant and a sketch variant. Some issues have more than that but none have less, so this will cover my bases.

From there I wrote a function to take those 5 digit numbers and generate a dictionary of metadata corresponding to those numbers, and then a followup function that just concatenates that dictionary with some input into a SQL insert statement. If you look at it step by step, and I did this really from bottom to top instead of top to bottom, it really made sense.

Here's how it ended up:

```python

def issue_generator(lst):
# generates DC's 5 digit UPC codes for 4 printings
	for number in lst:
		batman_issues.append(str(number)+'1'+'1')
		batman_issues.append(str(number)+'1'+'2')
		batman_issues.append(str(number)+'2'+'1')
		batman_issues.append(str(number)+'3'+'1')


def metadata_generator(lst):
# uses the generated numbers to create a list of dictionaries holding metadata
# that corresponds to the schema
	for issue in lst:
		if issue[3] == '1':		
			variant = False
			cover_artist = 'Greg Capullo'
		if issue[3] == '2':
			variant = True
			cover_artist = 'Guest Artist'
		if issue[3] == '3':
			variant = True
			cover_artist = 'Greg Capullo'
		bat_dict = {
			'id' : issue,
			'issue_num' : str(issue[0:3]),
			'printing' : str(issue[4]),
			'variant' : str(variant),
			'cover artist' : cover_artist
		}
		list_with_metadata.append(bat_dict)
	
	
def SQL_insert_generator(dct):
# generates SQL insert statements for an existing MySQL schema using the dicts created
# in the metadata_generator function
	for lst in dct:
		print "INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('" + lst['id'] + "','Batman (2011)','" + lst['issue_num'] + "','" + lst['variant'] + "','" + lst['printing'] + "','" + lst['cover artist'] + "')"




bat_numbers=['001','002','003','004','005','006','007','008','009','010','011','012','013','014','015','016','017','018','019','020','021','022','023']
batman_issues=[]
list_with_metadata =[]

issue_generator(bat_numbers)

metadata_generator(batman_issues)

SQL_insert_generator(list_with_metadata)
```
This generated a full list of SQL insert statements for me, as seen below.

```
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00111','Batman (2011)','001','False','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00112','Batman (2011)','001','False','2','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00121','Batman (2011)','001','True','1','Guest Artist')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00131','Batman (2011)','001','True','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00211','Batman (2011)','002','False','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00212','Batman (2011)','002','False','2','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00221','Batman (2011)','002','True','1','Guest Artist')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00231','Batman (2011)','002','True','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00311','Batman (2011)','003','False','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00312','Batman (2011)','003','False','2','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00321','Batman (2011)','003','True','1','Guest Artist')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00331','Batman (2011)','003','True','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00411','Batman (2011)','004','False','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00412','Batman (2011)','004','False','2','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00421','Batman (2011)','004','True','1','Guest Artist')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00431','Batman (2011)','004','True','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00511','Batman (2011)','005','False','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00512','Batman (2011)','005','False','2','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00521','Batman (2011)','005','True','1','Guest Artist')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00531','Batman (2011)','005','True','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00611','Batman (2011)','006','False','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00612','Batman (2011)','006','False','2','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00621','Batman (2011)','006','True','1','Guest Artist')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00631','Batman (2011)','006','True','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00711','Batman (2011)','007','False','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00712','Batman (2011)','007','False','2','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00721','Batman (2011)','007','True','1','Guest Artist')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00731','Batman (2011)','007','True','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00811','Batman (2011)','008','False','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00812','Batman (2011)','008','False','2','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00821','Batman (2011)','008','True','1','Guest Artist')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00831','Batman (2011)','008','True','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00911','Batman (2011)','009','False','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00912','Batman (2011)','009','False','2','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00921','Batman (2011)','009','True','1','Guest Artist')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('00931','Batman (2011)','009','True','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01011','Batman (2011)','010','False','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01012','Batman (2011)','010','False','2','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01021','Batman (2011)','010','True','1','Guest Artist')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01031','Batman (2011)','010','True','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01111','Batman (2011)','011','False','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01112','Batman (2011)','011','False','2','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01121','Batman (2011)','011','True','1','Guest Artist')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01131','Batman (2011)','011','True','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01211','Batman (2011)','012','False','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01212','Batman (2011)','012','False','2','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01221','Batman (2011)','012','True','1','Guest Artist')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01231','Batman (2011)','012','True','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01311','Batman (2011)','013','False','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01312','Batman (2011)','013','False','2','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01321','Batman (2011)','013','True','1','Guest Artist')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01331','Batman (2011)','013','True','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01411','Batman (2011)','014','False','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01412','Batman (2011)','014','False','2','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01421','Batman (2011)','014','True','1','Guest Artist')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01431','Batman (2011)','014','True','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01511','Batman (2011)','015','False','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01512','Batman (2011)','015','False','2','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01521','Batman (2011)','015','True','1','Guest Artist')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01531','Batman (2011)','015','True','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01611','Batman (2011)','016','False','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01612','Batman (2011)','016','False','2','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01621','Batman (2011)','016','True','1','Guest Artist')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01631','Batman (2011)','016','True','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01711','Batman (2011)','017','False','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01712','Batman (2011)','017','False','2','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01721','Batman (2011)','017','True','1','Guest Artist')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01731','Batman (2011)','017','True','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01811','Batman (2011)','018','False','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01812','Batman (2011)','018','False','2','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01821','Batman (2011)','018','True','1','Guest Artist')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01831','Batman (2011)','018','True','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01911','Batman (2011)','019','False','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01912','Batman (2011)','019','False','2','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01921','Batman (2011)','019','True','1','Guest Artist')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('01931','Batman (2011)','019','True','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('02011','Batman (2011)','020','False','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('02012','Batman (2011)','020','False','2','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('02021','Batman (2011)','020','True','1','Guest Artist')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('02031','Batman (2011)','020','True','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('02111','Batman (2011)','021','False','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('02112','Batman (2011)','021','False','2','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('02121','Batman (2011)','021','True','1','Guest Artist')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('02131','Batman (2011)','021','True','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('02211','Batman (2011)','022','False','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('02212','Batman (2011)','022','False','2','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('02221','Batman (2011)','022','True','1','Guest Artist')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('02231','Batman (2011)','022','True','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('02311','Batman (2011)','023','False','1','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('02312','Batman (2011)','023','False','2','Greg Capullo')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('02321','Batman (2011)','023','True','1','Guest Artist')
INSERT INTO `issue` (`id`,`title`,`issue_num`,`variant`,`printing`,`cover_artist`) VALUES ('02331','Batman (2011)','023','True','1','Greg Capullo')
```

And now I can feed that directly into my MySQL database and all that remains is to input the ownership table, which I'll use to track what comics I've bought and how much I paid for them.

Overall, it probably took me longer to figure this out than it would've to do by hand. But still! Learning! 
