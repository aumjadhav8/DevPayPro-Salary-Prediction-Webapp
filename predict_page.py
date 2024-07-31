import streamlit as st
import pickle
import numpy as np
from streamlit_text_rating.st_text_rater import st_text_rater

@st.cache_data
def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data['model']
le_country = data['le_country']
le_edLevel = data['le_edLevel']
le_remoteWork = data['le_remoteWork']

def show_predict_page():
    st.title("Developers Salary Prediction")

    st.write("""#### Please provide some information to us in order to predict the salary""")

    countries = ("United States of America",
                "Germany",
                "United Kingdom of Great Britain and Northern Ireland",
                "India",
                "Canada",
                "Brazil",
                "France",
                "Spain",
                "Netherlands",
                "Italy",
                "Australia",
                "Poland")

    education = ("Bachelor's degree", 
                "Master's degree", 
                "Less than a Bachelors",
                "Postgraduate")

    remoteWork = ("Full in-person",
                "Fully remote",
                "Hybrid (some remote, some in-person)")

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education", education)
    remoteWork = st.selectbox("Work Mode", remoteWork)

    code_experience = st.slider("Years of Coding Experience", 0, 50, 5)
    work_experience = st.slider("Years of Working Experience", 0, 40, 1)

    def checkbox_columns(category, items):
        cols = st.columns(2)
        with cols[0]:
            st.write(f"Worked with in PAST year")
            past = {item: st.checkbox(f"{item}", key=f"{item}_past_{category}") for item in items}
        with cols[1]:
            st.write(f"Want to work with NEXT year")
            next = {item: st.checkbox(f"{item}", key=f"{item}_next_{category}") for item in items}
        return past, next

    st.write("### Programming, Scripting, and Markup Languages")
    languages = ["Ada", "Apex", "APL", "Assembly", "Bash/Shell (all shells)", "C", "C#", "C++", "Clojure", "Cobol", "Crystal", "Dart", "Delphi", "Elixir", "Erlang", "F#", "Flow", "Fortran", "GDScript", "Go", "Groovy", "Haskell", "HTML/CSS", "Java", "JavaScript", "Julia", "Kotlin", "Lisp", "Lua", "MATLAB", "Nim", "Objective-C", "OCaml", "Perl", "PHP", "PowerShell", "Prolog", "Python", "R", "Raku", "Ruby", "Rust", "SAS", "Scala", "Solidity", "SQL", "Swift", "TypeScript", "VBA", "Visual Basic (.Net)", "Zig", "Other"]
    language_past, language_next = checkbox_columns("languages", languages)

    st.write("### Database Environments")
    databases = ["BigQuery", "Cassandra", "Clickhouse", "Cloud Firestore", "Cockroachdb", "Cosmos DB", "Couch DB", "Couchbase", "Datomic", "DuckDB", "Dynamodb", "Elasticsearch", "Firebase Realtime Database", "Firebird", "H2", "IBM DB2", "InfluxDB", "MariaDB", "Microsoft Access", "Microsoft SQL Server", "MongoDB", "MySQL", "Neo4J", "Oracle", "PostgreSQL", "RavenDB", "Redis", "Snowflake", "Solr", "SQLite", "Supabase", "TiDB", "Other"]
    db_past, db_next = checkbox_columns("databases", databases)

    st.write("### Cloud Platforms")
    clouds = ["Amazon Web Services (AWS)", "Cloudflare", "Colocation", "Digital Ocean", "Firebase", "Fly.io", "Google Cloud", "Heroku", "Hetzner", "IBM Cloud Or Watson", "Linode", "Managed Hosting", "Microsoft Azure", "Netlify", "OpenShift", "OpenStack", "Oracle Cloud Infrastructure (OCI)", "OVH", "Render", "Scaleway", "Vercel", "VMware", "Vultr", "Other"]
    cloud_past, cloud_next = checkbox_columns("clouds", clouds)

    st.write("### Web Frameworks and Web Technologies")
    web_frameworks = ["Angular", "AngularJS", "ASP.NET", "ASP.NET CORE", "Blazor", "CodeIgniter", "Deno", "Django", "Drupal", "Elm", "Express", "FastAPI", "Fastify", "Flask", "Gatsby", "jQuery", "Laravel", "Lit", "NestJS", "Next.js", "Node.js", "Nuxt.js", "Phoenix", "Play Framework", "Qwik", "React", "Remix", "Ruby on Rails", "Solid.js", "Spring Boot", "Svelte", "Symfony", "Vue.js", "WordPress", "Other"]
    web_past, web_next = checkbox_columns("web_frameworks", web_frameworks)

    st.write("### Other Frameworks and Libraries")
    frameworks = [".NET (5+)", ".NET Framework (1.0 - 4.8)", ".NET MAUI", "Apache Kafka", "Apache Spark", "Capacitor", "Cordova", "CUDA", "Electron", "Flutter", "GTK", "Hadoop", "Hugging Face Transformers", "Ionic", "JAX", "Keras", "Ktor", "MFC", "Micronaut", "Numpy", "Opencv", "OpenGL", "Pandas", "Qt", "Quarkus", "RabbitMQ", "React Native", "Scikit-Learn", "Spring Framework", "SwiftUI", "Tauri", "TensorFlow", "Tidyverse", "Torch/PyTorch", "Uno Platform", "Xamarin", "Other"]
    framework_past, framework_next = checkbox_columns("frameworks", frameworks)

    st.write("### Developer Tools for Compiling, Building and Testing")
    tools = ["Ansible", "Ant", "APT", "bandit", "Boost.Test", "build2", "Bun", "Cargo", "Catch2", "Chef", "Chocolatey", "CMake", "Composer", "cppunit", "CUTE", "Dagger", "Docker", "doctest", "ELFspy", "GNU GCC", "Godot", "Google Test", "Gradle", "Homebrew", "Kubernetes", "lest", "liblittletest", "LLVM's Clang", "Make", "Maven (build tool)", "Meson", "MSBuild", "MSVC", "Ninja", "Nix", "npm", "NuGet", "Pacman", "Pip", "pnpm", "Podman", "Pulumi", "Puppet", "QMake", "SCons", "snitch", "Terraform", "tunit", "Unity 3D", "Unreal Engine", "Visual Studio Solution", "Vite", "Wasmer", "Webpack", "Yarn", "Other"]
    tool_past, tool_next = checkbox_columns("tools", tools)

    st.write("### Development Environments")
    environments = ["Android Studio", "Atom", "BBEdit", "CLion", "Code::Blocks", "condo", "DataGrip", "Eclipse", "Emacs", "Fleet", "Geany", "Goland", "Helix", "IntelliJ IDEA", "IPython", "Jupyter Notebook/JupyterLab", "Kate", "Micro", "Nano", "Neovim", "Netbeans", "Notepad++", "Nova", "PhpStorm", "PyCharm", "Qt Creator", "Rad Studio (Delphi, C++ Builder)", "Rider", "RStudio", "RubyMine", "Spyder", "Sublime Text", "TextMate", "Vim", "Visual Studio", "Visual Studio Code", "VSCodium", "WebStorm", "Xcode", "Other"]
    env_past, env_next = checkbox_columns("environments", environments)

    st.write("### Primary Operating System")
    os_options = ["AIX", "Android", "Arch", "BSD", "ChromeOS", "Cygwin", "Debian", "Fedora", "Haiku", "iOS", "iPadOS", "MacOS", "Other Linux-based", "Red Hat", "Solaris", "Ubuntu", "Windows", "Windows Subsystem for Linux (WSL)", "Other"]
    os_personal, os_professional = checkbox_columns("os", os_options)

    st.write("### Collaborative Work Management and/or Code Documentation Tools")
    collaboration_tools = ["Adobe Workfront", "Airtable", "Asana", "Azure Devops", "Basecamp", "Cerri", "Clickup", "Confluence", "Dingtalk (Teambition)", "Document360", "Doxygen", "GitHub Discussions", "Jira", "Leankor", "Linear", "Markdown File", "Microsoft Lists", "Microsoft Planner", "Miro", "Monday.com", "Notion", "Nuclino", "Planview Projectplace Or Clarizen", "Redmine", "Redocly", "Shortcut", "Smartsheet", "Stack Overflow for Teams", "Swit", "Tettra", "Trello", "Wikis", "Wimi", "Workzone", "Wrike", "YouTrack", "Other"]
    collab_past, collab_next = checkbox_columns("collaboration_tools", collaboration_tools)

    st.write("### Communication Tools")
    communication_tools = ["Cisco Webex Teams", "Coolfire Core", "Discord", "Google Chat", "Google Meet", "IRC", "Jitsi", "Matrix", "Mattermost", "Microsoft Teams", "Ringcentral", "Rocketchat", "Signal", "Skype", "Slack", "Symphony", "Telegram", "Unify Circuit", "Whatsapp", "Wickr", "Wire", "Zoom", "Zulip", "Other"]
    comm_past, comm_next = checkbox_columns("communication_tools", communication_tools)

    st.write("### AI-Powered Search Tools")
    ai_search_tools = ["Andi", "Bing AI", "ChatGPT", "Google Bard AI", "Metaphor", "Neeva AI", "Perplexity AI", "Phind", "Quora Poe", "WolframAlpha", "You.com", "Other"]
    ai_search_past, ai_search_next = checkbox_columns("ai_search_tools", ai_search_tools)

    st.write("### AI-Powered Developer Tools")
    ai_dev_tools = ["Adrenaline", "AWS CodeWhisperer", "Codeium", "GitHub Copilot", "Mintlify", "Replit Ghostwriter", "Rubber Duck.AI", "Synk Code", "Tabnine", "Whispr AI", "Other"]
    ai_dev_past, ai_dev_next = checkbox_columns("ai_dev_tools", ai_dev_tools)

    enter = st.button("Predict Salary")
    if enter:
        X = np.array([[country, education, remoteWork, code_experience, work_experience]])
        X[:, 0] = le_country.transform(X[:, 0])
        X[:, 1] = le_edLevel.transform(X[:, 1])
        X[:, 2] = le_remoteWork.transform(X[:, 2])
        X = X.astype(float)

        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")

        st.markdown("Awesome App ?")
        for text in ["Is this helpful?"]:
            response = st_text_rater(text=text)

if __name__ == "__main__":
    show_predict_page()
