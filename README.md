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

For the **initial start up**, we need to define a Postgres server password, create clinical data database, fill out its schema, and populate it with test and sample data. To do that, run the following. (Looks like we're keeping this secret password in the file `postgres-passwd.txt`.)

First, make a directory to hold the data:

    mkdir -p /usr/local/labcas/mcl/clinic/docker-data/postgresql

Start the system with the secret password:

    env \
        POSTGRES_PASSWORD=$(cat postgres-passwd.txt) \
        docker-compose \
        --project-name clinic \
        up \
        --detach

Create the `mcl` database user:

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

    docker-compose --project-name clinic down

Then start it as you would routinely start it, described in the next section.


### 🏃‍♀️ Regular Running

After the initial startup (above), here's what you need to do to get things running normally:

    docker-compose --project-name clinic up --detach

You can check on things with:

    docker-compose --project-name clinic logs

You can see if it's answering locally with:

    curl -s http://localhost:6543/ping | json_pp

Need to bring it down? Just do this:

    docker-compose --project-name clinic down

Back up the database:

    docker-compose \
        --project-name clinic \
        exec \
        db \
            pg_dump \
                --dbname=clinical_data \
                --username=mcl \
                --encoding=UTF8 \
                --password  > some-backup.sql

Nothing happening? That's because it's waiting for a password whose prompt got swallowed into the `some-backup.sql` file. Go ahead and enter it, then edit `some-backup.sql` and remove the prompt. Also, copy the file `some-backup.sql` to a better name and to a safer system.


### 🌱 Environment

By default, the `docker-compose.yaml` is set up to run the production instance of the Clinical Data application on `edrn-docker.jpl.nasa.gov`. You can specify the following environment variables to override settings; this is typically only needed in development:

- `CLINICAL_API_PORT`: This defaults to 6543, to which the front-end web server for `https://mcl.jpl.nasa.gov/infirmary` reverse-proxies in order to provide access to the Clinical Data API.
- `CLINICAL_API_V1_VERSION`: This defaults to `1.0.0`, but you can override this with a specific tag if needed.
- `CLINICAL_API_V2_VERSION`: This defaults to `1.0.2`, but you can override this with a specific tag if needed.
- `CLINICAL_API_V3_VERSION`: This defaults to `latest`, but you can and should override this with a specific tag.
- `CLINICAL_DATA_DIR`: This tells where to find the PostgreSQL data volume; it's usually set to `/usr/local/labcas/mcl/clinic/docker-data` and there should be a `postgresql` directory inside of it.
- `CLINICAL_DB_PORT`: This defaults to 5432, which is the usual TCP port for PostgreSQL. You'll almost never need to change this.
- `MCL_IMAGE_OWNER`: This defaults to `nutjob4life/` but you can set it to an empty string in order to make Docker use your local image repository.


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
