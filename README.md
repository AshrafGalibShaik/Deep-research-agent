# DeepResearch Agent 🔍

A specialized AI research agent designed to analyze and compare developer tools, technologies, and programming platforms. Built with LangGraph workflows and powered by Google's Gemini AI, this agent provides comprehensive analysis of tech stacks, pricing models, and developer experience insights.

## ✨ Features

- **Intelligent Tool Discovery**: Automatically extracts relevant developer tools from articles and search results
- **Comprehensive Analysis**: Analyzes pricing models, tech stacks, language support, and API availability
- **Developer-Focused Research**: Specializes in programming tools, frameworks, libraries, and platforms
- **Structured Output**: Returns organized data with clear recommendations
- **Multi-Source Research**: Combines search results with detailed web scraping for accurate information

## 🛠️ Technology Stack

- **LangGraph**: Workflow orchestration and state management
- **Google Gemini 2.0**: AI model for analysis and structured output
- **Firecrawl**: Web scraping and search capabilities
- **Pydantic**: Data validation and modeling
- **Python**: Core implementation language

## 📋 Prerequisites

- Python 3.8+
- Firecrawl API key
- Google Gemini API key

## 🚀 Installation

1. **Clone the repository**:
```bash
git clone <repository-url>
cd deepresearch-agent
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**:
Create a `.env` file in the root directory:
```env
FIRECRAWL_API_KEY=your_firecrawl_api_key_here
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

4. **Install required packages**:
```bash
pip install firecrawl-py langgraph langchain-google-genai python-dotenv pydantic
```

## 🎯 Usage

### Command Line Interface

Run the interactive CLI:
```bash
python main.py
```

### Example Queries

The agent works best with developer-focused queries:

- `"Python web frameworks"`
- `"No-code database solutions"`
- `"JavaScript testing libraries"`
- `"Cloud hosting platforms"`
- `"API documentation tools"`
- `"React state management libraries"`

### Sample Output

```
📊 Results for: Python web frameworks

1. 🏢 FastAPI
   🌐 Website: https://fastapi.tiangolo.com
   💰 Pricing: Free
   📖 Open Source: True
   🛠️  Tech Stack: Python, Starlette, Pydantic, OpenAPI, JSON Schema
   💻 Language Support: Python
   🔌 API: ✅ Available
   🔗 Integrations: SQLAlchemy, PostgreSQL, MongoDB, Redis
   📝 Description: Modern, fast web framework for building APIs with Python

2. 🏢 Django
   🌐 Website: https://www.djangoproject.com
   💰 Pricing: Free
   📖 Open Source: True
   🛠️  Tech Stack: Python, SQLite, PostgreSQL, MySQL, Redis
   💻 Language Support: Python
   🔌 API: ✅ Available
   🔗 Integrations: PostgreSQL, Redis, Celery, Docker
   📝 Description: High-level Python web framework for rapid development

Developer Recommendations:
FastAPI is the best choice for modern API development due to its automatic OpenAPI documentation and excellent performance. Both are free and open-source. FastAPI offers superior developer experience with built-in validation and modern Python features.
```

## 🏗️ Architecture

### Workflow Steps

1. **Tool Extraction**: Searches for articles about the query topic and extracts specific tool names
2. **Research**: Investigates each discovered tool by scraping official websites
3. **Analysis**: Uses structured AI analysis to extract developer-relevant information
4. **Recommendations**: Generates concise recommendations based on findings

### Key Components

- **`Workflow`**: Main orchestrator using LangGraph state management
- **`FirecrawlService`**: Handles web searching and scraping operations
- **`CompanyInfo`**: Data model for tool/company information
- **`CompanyAnalysis`**: Structured analysis output from AI
- **`DeveloperToolsPrompts`**: Specialized prompts for developer tool analysis

## 📊 Data Model

### CompanyInfo
```python
class CompanyInfo(BaseModel):
    name: str
    description: str
    website: str
    pricing_model: Optional[str]  # Free, Freemium, Paid, Enterprise
    is_open_source: Optional[bool]
    tech_stack: List[str]
    api_available: Optional[bool]
    language_support: List[str]
    integration_capabilities: List[str]
    developer_experience_rating: Optional[str]
```

### Analysis Focus Areas

- **Pricing Models**: Free, Freemium, Paid, Enterprise pricing structures
- **Open Source Status**: Whether tools are open source or proprietary
- **Technology Stack**: Programming languages, frameworks, databases supported
- **API Availability**: REST APIs, GraphQL, SDKs, programmatic access
- **Language Support**: Specific programming languages supported
- **Integrations**: Compatible tools, platforms, and services

## ⚙️ Configuration

### Environment Variables

- `FIRECRAWL_API_KEY`: Your Firecrawl API key for web scraping
- `GOOGLE_API_KEY`: Your Google Gemini API key for AI analysis

### Customization Options

- **Search Results Limit**: Modify `num_results` in search functions
- **Content Analysis Depth**: Adjust content truncation limits
- **Tool Extraction Count**: Change the number of tools analyzed per query
- **AI Model**: Switch between different Gemini models in workflow.py

## 🔧 API Reference

### FirecrawlService

```python
# Search for companies/tools
results = firecrawl.search_companies(query, num_results=5)

# Scrape specific URLs
content = firecrawl.scrape_company_pages(url)
```

### Workflow

```python
# Run complete research workflow
workflow = Workflow()
result = workflow.run("your developer tools query")
```

## 🚨 Limitations

- Requires active internet connection for web scraping
- API rate limits may apply depending on your Firecrawl/Gemini usage
- Analysis quality depends on the availability and quality of web content
- Some websites may block scraping attempts

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🛟 Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Check existing documentation
- Review the code comments for implementation details

## 🔮 Future Enhancements

- **Caching System**: Implement Redis caching for repeated queries
- **Export Functionality**: Add CSV/JSON export for research results
- **Comparison Matrix**: Visual comparison tables for multiple tools
- **Historical Analysis**: Track pricing and feature changes over time
- **Integration Scoring**: Quantitative scoring for developer experience
- **Custom Filters**: Filter results by pricing, language, or features

---


