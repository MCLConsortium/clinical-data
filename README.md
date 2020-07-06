# 🧪 Clinical Data

This is repository for the Consortium for Molecular and Cellular Characterization of Screen-Detected Lesions' **Clinical Data** application, including:

- A clinical data database
- An OODT micro-service for
- And a web-based analysis application

Or we might break this into three separate repositories. This is all up in the air right now.


## 🚙 Getting Started

Well you can run `db.sh` to create a local PostgreSQL database. You can then access it with:

    psql --username=mcl --no-password clinical_data

Or from SQLAlchemy with:

```python
from sqlalchemy import create_engine
engine = create_engine('postgresql://mcl@localhost/clinical_data')
```


## 📀 Software Environment

We're still figuring this out. 🤔

For now, there's a budding prototype in the `sickbay` subdirectory.


### 👥 Contributing

Well it's wide open right now, but later you might look at [open issues](https://github.com/MCLConsortium/clinical-data/issues), forking the project, and submitting a pull request.


### 🔢 Versioning

We use the [SemVer](https://semver.org/) philosophy for versioning this software. For versions available, see the [releases made](https://github.com/MCLConsortium/clinical-data/releases) on this project.


## 📃 License

The project is licensed under the [Apache version 2](LICENSE.txt) license.
