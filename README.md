# 🧪 Clinical Data

This is repository for the Consortium for Molecular and Cellular Characterization of Screen-Detected Lesions' **Clinical Data** application, including:

- A clinical data database ([PostgreSQL](https://www.postgresql.org/))
- An OODT micro-service for populating the database, [TBD](mailto:Asitang.Mishra@jpl.nasa.gov)
- A ReST API, [Infirmary](https://pypi.org/project/mcl.infirmary/)
- A web-based analysis application, [TBD](mailto:David.Liu@jpl.nasa.gov)
- An object API and object-relational mapping, [Sickbay](https://pypi.org/project/mcl.sickbay/)


## 🚙 Getting Started

This section tells how to get this software going.


### 👶 Initial Start

For the **initial start up**, we need to define a Postgres server password, create clinical data database, fill out its schema, and populate it with test and sample data. To do that, run the following, and replace `SECRET` with a top-secret password for Postgres.

First, make a directory to hold the data:

    mkdir -p /usr/local/labcas/mcl/clinic/docker-data/postgresql

Start the system with the `SECRET` password:

    env \
        POSTGRES_PASSWORD=SECRET \
        CLINICAL_DB_PORT=5432 \
        CLINICAL_API_PORT=6543 \
        CLINICAL_DATA_DIR=/usr/local/labcas/mcl/clinic/docker-data \
        docker-compose \
        --project-name clinic \
        up \
        --detach

Create the `mcl` database user:

    env \
        CLINICAL_DB_PORT=5432 \
        CLINICAL_API_PORT=6543 \
        CLINICAL_DATA_DIR=/usr/local/labcas/mcl/clinic/docker-data \
        docker-compose \
        --project-name clinic \
        exec \
        db \
        createuser \
            --username=postgres \
            --createdb \
            --inherit \
            --login \
            --no-createrole \
            --no-superuser \
            --pwprompt \
            mcl        

When prompted, enter a password for the user, the same as the username. (Enter it twice.) Then, create the empty database:

    env \
        CLINICAL_DB_PORT=5432 \
        CLINICAL_API_PORT=6543 \
        CLINICAL_DATA_DIR=/usr/local/labcas/mcl/clinic/docker-data \
        docker-compose \
        --project-name clinic \
        exec \
        db \
        createdb \
            --username=postgres \
            --encoding=UTF8 \
            --owner=mcl \
            clinical_data

And fill out its schema and sample data:

    env \
        CLINICAL_DB_PORT=5432 \
        CLINICAL_API_PORT=6543 \
        CLINICAL_DATA_DIR=/usr/local/labcas/mcl/clinic/docker-data \
        docker-compose \
        --project-name clinic \
        exec \
        api \
        create-clinical-db \
            --host db \
            --password \
            --add-test-data \
            --add-sample-data

When prompted, use the same password as you entered when prompted above. Now shut it all down:

    env \
        CLINICAL_DB_PORT=5432 \
        CLINICAL_API_PORT=6543 \
        CLINICAL_DATA_DIR=/usr/local/labcas/mcl/clinic/docker-data \
        docker-compose \
        --project-name clinic \
        down

Then start it as you would routinely start it, described in the next section.


### 🏃‍♀️ Regular Running

After the initial startup (above), here's what you need to do to get things running normally:

    env \
        CLINICAL_DB_PORT=5432 \
        CLINICAL_API_PORT=6543 \
        CLINICAL_DATA_DIR=/usr/local/labcas/mcl/clinic/docker-data \
        docker-compose \
        --project-name clinic \
        up \
        --detach

You can check on things with:

    env \
        CLINICAL_DB_PORT=5432 \
        CLINICAL_API_PORT=6543 \
        CLINICAL_DATA_DIR=/usr/local/labcas/mcl/clinic/docker-data \
        docker-compose \
        --project-name clinic \
        logs

You can see if it's answering locally with:

    curl -s http://localhost:6543/ping | json_pp

Need to bring it down? Just do this:

    env \
        CLINICAL_DB_PORT=5432 \
        CLINICAL_API_PORT=6543 \
        CLINICAL_DATA_DIR=/usr/local/labcas/mcl/clinic/docker-data \
        docker-compose \
        --project-name clinic \
        down


## 📀 Software Environment

We're still figuring this out. 🤔

So far, though, we have:

-   Sickbay, which is the data model and ORM, available on [PyPI](https://pypi.org/project/mcl.sickbay/) and [GitHub](https://github.com/MCLConsortium/mcl.sickbay). This serves as the **definitive** database schema and class-based representation of clinical data, and is used by the ReST API to provide the data and the OODT microservice to ingest the data.
-   Infirmary, which is the ReST API for providing the clinical data to the user interface and other future clients. It's avaialbe on [PyPI](https://pypi.org/project/mcl.infirmary/) and [GitHub](https://github.com/MCLConsortium/mcl.infirmary).
-   OODT micro service. [TBD](mailto:Asitang.Mishra@jpl.nasa.gov).
-   User interface. [TBD](mailto:David.Liu@jpl.nasa.gov).


### 📦 Resources

Here are some handy links:

-   The [Google Drive](http://bit.ly/mcl-clinical-drive) has sample data, presentations, mockups, etc.
-   [Common Data Elements](https://mcl.nci.nih.gov/resources/standards/mcl-cdes)
-   We also have a mailing list: [mcl-clinical-data@jpl.nasa.gov](mailto:mcl-clinical-data@jpl.nasa.gov)


### 👥 Contributing

Well it's wide open right now, but later you might look at [open issues](https://github.com/MCLConsortium/clinical-data/issues), forking the project, and submitting a pull request.


### 🔢 Versioning

We use the [SemVer](https://semver.org/) philosophy for versioning this software. For versions available, see the [releases made](https://github.com/MCLConsortium/clinical-data/releases) on this project.


## 📃 License

The project is licensed under the [Apache version 2](LICENSE.txt) license.
