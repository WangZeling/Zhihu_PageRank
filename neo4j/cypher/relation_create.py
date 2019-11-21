# Create relationships in CSV based on existing entities
LOAD CSV WITH HEADERS  FROM "file:///zhihu06.csv" AS row
MATCH (a:zhihu),(b:zhihu)
where a.name=row.f1 AND b.name=row.f2
create (a)-[r:torel{torel:'to'}]->(b)

# Query hierarchical node:
match q=(x)-[*5..8]-() return q limit 200
# Query such hierarchical node:
match q=(dh)-[r]-(jq)-[rr]-()-[]-()-[]-()-[]-()-[]-()-[]-() return q limit 400
# Query node:
MATCH p=()-[r:torel]->() RETURN p LIMIT 250
# Query the node associated with the heart of the machine
match (n)--(m:zhihuEntity {name:' »úÆ÷Ö®ÐÄ '}) return n,m
