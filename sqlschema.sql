DROP TABLE IF EXISTS applications;

CREATE TABLE applications (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  app_name TEXT NOT NULL,
  email TEXT NOT NULL,
  job_title TEXT NOT NULL,
  job_description TEXT NOT NULL
 
  
);
