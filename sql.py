# Fill in credentials
host='data-analytics-course.c8g8r1deus2v.eu-central-1.rds.amazonaws.com'
port='5432'
database='postgres'
user='maximilianpiepelow'
password='wPdcAV7K3LZxbqSn'


from sqlalchemy import create_engine    
engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')

# Import the Python packages for get_data() function



# Insert the get_data() function definition below
