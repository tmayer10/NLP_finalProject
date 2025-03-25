import os
import re
import shutil
import subprocess
from pathlib import Path

class OverleafProject:
    def __init__(self, project_name, author_name, template="article"):
        """
        Initialize an Overleaf project structure for an academic paper.
        
        Args:
            project_name (str): Name of the academic paper/project
            author_name (str): Author's name
            template (str): LaTeX template to use (default: article)
        """
        self.project_name = project_name
        self.author_name = author_name
        self.template = template
        self.root_dir = Path(f"{project_name.replace(' ', '_')}_overleaf")
        
        # Create project directories
        self.create_directory_structure()
        
    def create_directory_structure(self):
        """Create the standard directory structure for an academic paper."""
        # Create main directory
        os.makedirs(self.root_dir, exist_ok=True)
        
        # Create subdirectories
        subdirs = ["figures", "tables", "sections", "references", "data"]
        for subdir in subdirs:
            os.makedirs(self.root_dir / subdir, exist_ok=True)
            
        # Create initial files
        self.create_main_tex_file()
        self.create_bibliography_file()
        self.create_section_files()
        
    def create_main_tex_file(self):
        """Create the main.tex file with proper structure."""
        main_tex_content = f"""\\documentclass{{{self.template}}}

% Packages
\\usepackage[utf8]{{inputenc}}
\\usepackage[english]{{babel}}
\\usepackage{{graphicx}}
\\usepackage{{amsmath}}
\\usepackage{{amssymb}}
\\usepackage{{natbib}}
\\usepackage{{hyperref}}
\\usepackage{{booktabs}}
\\usepackage{{float}}
\\usepackage{{url}}

% Document information
\\title{{{self.project_name}}}
\\author{{{self.author_name}}}
\\date{{\\today}}

\\begin{{document}}

\\maketitle

\\begin{{abstract}}
% Your abstract goes here
This paper examines the role of NFL commentators in fan engagement and profit maximization. Using data analysis, we explore how commentating styles have evolved over time and develop predictive models for commentator behavior.
\\end{{abstract}}

% Include sections
\\input{{sections/introduction}}
\\input{{sections/literature_review}}
\\input{{sections/methodology}}
\\input{{sections/results}}
\\input{{sections/discussion}}
\\input{{sections/conclusion}}

% Bibliography
\\bibliographystyle{{apalike}}
\\bibliography{{references/bibliography}}

\\end{{document}}
"""
        with open(self.root_dir / "main.tex", "w") as f:
            f.write(main_tex_content)
            
    def create_bibliography_file(self):
        """Create a sample bibliography file."""
        bib_content = """@article{example2023,
  title={Example Article Title},
  author={Author, A. and Writer, B.},
  journal={Journal of Examples},
  volume={1},
  number={1},
  pages={1--10},
  year={2023},
  publisher={Example Publisher}
}

@book{nfl2022,
  title={NFL Broadcasting and Fan Engagement},
  author={Smith, John and Johnson, Robert},
  year={2022},
  publisher={Sports Publishing},
  address={New York}
}
"""
        with open(self.root_dir / "references" / "bibliography.bib", "w") as f:
            f.write(bib_content)
            
    def create_section_files(self):
        """Create template files for each section."""
        sections = {
            "introduction": "\\section{Introduction}\nThe NFL is a billion-dollar league. To quote the movie \"Concussion\" starring Will Smith, the league \"practically owns a day of the week\"\n\nCommentating is a crucial task for the NFL to engage fans and provide a better experience. The goal of commentating is to provide a clear and engaging narrative of the game.",
            "literature_review": "\\section{Literature Review}\n% Your literature review content here",
            "methodology": "\\section{Methodology}\n% Your methodology content here",
            "results": "\\section{Results}\n% Your results content here",
            "discussion": "\\section{Discussion}\n% Your discussion content here",
            "conclusion": "\\section{Conclusion}\n% Your conclusion content here"
        }
        
        for section_name, content in sections.items():
            with open(self.root_dir / "sections" / f"{section_name}.tex", "w") as f:
                f.write(content)
                
    def export_to_zip(self, output_path=None):
        """
        Export the project to a zip file for uploading to Overleaf.
        
        Args:
            output_path (str, optional): Path to save the zip file. Defaults to current directory.
        
        Returns:
            str: Path to the created zip file
        """
        if output_path is None:
            output_path = os.getcwd()
            
        zip_path = os.path.join(output_path, f"{self.project_name.replace(' ', '_')}.zip")
        shutil.make_archive(
            os.path.splitext(zip_path)[0],
            'zip',
            self.root_dir.parent,
            self.root_dir.name
        )
        return zip_path
    
    def __str__(self):
        return f"Overleaf Project: {self.project_name} by {self.author_name}"


def create_nfl_commentary_paper():
    """Create a pre-configured project for NFL commentary analysis."""
    project = OverleafProject(
        "NFL Commentary Analysis: Impact on Fan Engagement and Profit",
        "Your Name",
        template="article"
    )
    
    # Add custom content to introduction
    intro_path = project.root_dir / "sections" / "introduction.tex"
    with open(intro_path, "r") as f:
        intro_content = f.read()
    
    # Append additional content from Introduction.txt
    additional_content = """
The NFL, a for-profit organization, is a profit-maximizing firm. Do the commentators play a role in the engagement of fans and therefore, profit? If so, how can we use data to optimize the commentating?

My uncle, Brandon Cruse, is a referee for the NFL. Sometimes, he reminds me how much the game changes every year - the rules, the plays, the fans' expectations. With fans at the forefront of the NFL's strategy, the league changes rules almost every year to keep the game exciting and engaging. I'm interested in how the commentating changes to keep up with the game.

Commentary is just as important. In this project, I'm interested in how we can use data to optimize the commentating. How has it changed over time, if at all? How can we use data to predict the commentating style of a given commentator?
"""
    
    with open(intro_path, "w") as f:
        f.write(intro_content + additional_content)
    
    return project


if __name__ == "__main__":
    # Example usage
    project = create_nfl_commentary_paper()
    zip_path = project.export_to_zip()
    print(f"Project created and exported to {zip_path}")
    print("You can now upload this zip file to Overleaf.")
