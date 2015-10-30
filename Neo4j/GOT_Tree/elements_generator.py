import csv
from py2neo import authenticate,Graph
from py2neo import neo4j,Node,Relationship
import re
 
authenticate("localhost:7474", "neo4j", "neo4j1")

# connect to authenticated graph database
sgraph = Graph("http://localhost:7474/db/data/")

with open('C:\\Users\\brsingh\\Documents\\characters.csv','r') as csvfile:
	filereader = csv.DictReader(csvfile,delimiter=',')
	for row in filereader:
		'''char1 = Node("Character",Name=row['Name'])
		char1.properties['House'] = row['House']
		char1.properties['isDead'] = row['isDead']
		char1.properties['isCaptured'] = row['isCaptured']
		char1.properties['isHurt'] = row['isHurt']
		char1.properties["Title"] = row['title']
		char1.properties['prefix'] = row['prefix']
		char1.properties['characterId'] = row['characterID']
		sgraph.create(char1)
		sgraph.merge_one('Character',"Name",row['Name'])
		cursor.execute('MATCH (character1:Character {characterId:"' + row['relation1']+'"}) MATCH (character2:Character {characterId:"' + row['relation2'] + '"}) MERGE (character1.Name)-[:'+ row['relation'].upper() +']->(character2.Name)')
		connection.commit()'''
		'''creating text for command'''
		txtCommand = "CREATE (" + row['Name'].replace(' ','_') + ":Person {name : '" + row['Name'] + "', House : '" + row['House'] + "', isDead : " + row['isDead'] + ", isCaptured : " + row['isCaptured'] + ", isHurt : " + row['isHurt'] + ", Title : '" + row['title'] + "', Prefix : '" + row['prefix'] + "'})"
		'''sgraph.cypher.execute(txtCommand)'''
		print txtCommand