import requests
import bs4 
import pdb

from deep_translator import GoogleTranslator

GoogleTranslator(source='auto', target='es').translate("keep it up, you are awesome")

html_doc = '''<ul class="list-no-style">
                      <li class="main-nav-dropdown__item">
                        <a class="main-nav-dropdown__item-control color-charcoal" href="/subject/cs"
                          data-track-click="nav_click"
                          data-track-props="{&quot;type&quot;:&quot;Subject&quot;,&quot;title&quot;:&quot;Computer Science&quot;}"
                          data-track-ga="{&quot;category&quot;:&quot;nav_click&quot;,&quot;action&quot;:&quot;subject&quot;,&quot;label&quot;:&quot;Computer Science&quot;}"
                          data-name="NAV_SUBSECTION_PARENT"
                          data-detail="{&quot;childListId&quot;:&quot;subject-cs&quot;}">
                          <span>Computer Science</span>
                          <span class="main-nav-dropdown__item-icon icon-chevron-right-charcoal icon-small"></span>
                        </a>
                      </li>
                      <li class="main-nav-dropdown__item">
                        <a class="main-nav-dropdown__item-control color-charcoal" href="/subject/health"
                          data-track-click="nav_click"
                          data-track-props="{&quot;type&quot;:&quot;Subject&quot;,&quot;title&quot;:&quot;Health &amp; Medicine&quot;}"
                          data-track-ga="{&quot;category&quot;:&quot;nav_click&quot;,&quot;action&quot;:&quot;subject&quot;,&quot;label&quot;:&quot;Health &amp; Medicine&quot;}"
                          data-name="NAV_SUBSECTION_PARENT"
                          data-detail="{&quot;childListId&quot;:&quot;subject-health&quot;}">
                          <span>Health &amp; Medicine</span>
                          <span class="main-nav-dropdown__item-icon icon-chevron-right-charcoal icon-small"></span>
                        </a>
                      </li>
                      <li class="main-nav-dropdown__item">
                        <a class="main-nav-dropdown__item-control color-charcoal" href="/subject/maths"
                          data-track-click="nav_click"
                          data-track-props="{&quot;type&quot;:&quot;Subject&quot;,&quot;title&quot;:&quot;Mathematics&quot;}"
                          data-track-ga="{&quot;category&quot;:&quot;nav_click&quot;,&quot;action&quot;:&quot;subject&quot;,&quot;label&quot;:&quot;Mathematics&quot;}"
                          data-name="NAV_SUBSECTION_PARENT"
                          data-detail="{&quot;childListId&quot;:&quot;subject-maths&quot;}">
                          <span>Mathematics</span>
                          <span class="main-nav-dropdown__item-icon icon-chevron-right-charcoal icon-small"></span>
                        </a>
                      </li>
                      <li class="main-nav-dropdown__item">
                        <a class="main-nav-dropdown__item-control color-charcoal" href="/subject/business"
                          data-track-click="nav_click"
                          data-track-props="{&quot;type&quot;:&quot;Subject&quot;,&quot;title&quot;:&quot;Business&quot;}"
                          data-track-ga="{&quot;category&quot;:&quot;nav_click&quot;,&quot;action&quot;:&quot;subject&quot;,&quot;label&quot;:&quot;Business&quot;}"
                          data-name="NAV_SUBSECTION_PARENT"
                          data-detail="{&quot;childListId&quot;:&quot;subject-business&quot;}">
                          <span>Business</span>
                          <span class="main-nav-dropdown__item-icon icon-chevron-right-charcoal icon-small"></span>
                        </a>
                      </li>
                      <li class="main-nav-dropdown__item">
                        <a class="main-nav-dropdown__item-control color-charcoal" href="/subject/humanities"
                          data-track-click="nav_click"
                          data-track-props="{&quot;type&quot;:&quot;Subject&quot;,&quot;title&quot;:&quot;Humanities&quot;}"
                          data-track-ga="{&quot;category&quot;:&quot;nav_click&quot;,&quot;action&quot;:&quot;subject&quot;,&quot;label&quot;:&quot;Humanities&quot;}"
                          data-name="NAV_SUBSECTION_PARENT"
                          data-detail="{&quot;childListId&quot;:&quot;subject-humanities&quot;}">
                          <span>Humanities</span>
                          <span class="main-nav-dropdown__item-icon icon-chevron-right-charcoal icon-small"></span>
                        </a>
                      </li>
                      <li class="main-nav-dropdown__item">
                        <a class="main-nav-dropdown__item-control color-charcoal" href="/subject/engineering"
                          data-track-click="nav_click"
                          data-track-props="{&quot;type&quot;:&quot;Subject&quot;,&quot;title&quot;:&quot;Engineering&quot;}"
                          data-track-ga="{&quot;category&quot;:&quot;nav_click&quot;,&quot;action&quot;:&quot;subject&quot;,&quot;label&quot;:&quot;Engineering&quot;}"
                          data-name="NAV_SUBSECTION_PARENT"
                          data-detail="{&quot;childListId&quot;:&quot;subject-engineering&quot;}">
                          <span>Engineering</span>
                          <span class="main-nav-dropdown__item-icon icon-chevron-right-charcoal icon-small"></span>
                        </a>
                      </li>
                      <li class="main-nav-dropdown__item">
                        <a class="main-nav-dropdown__item-control color-charcoal" href="/subject/science"
                          data-track-click="nav_click"
                          data-track-props="{&quot;type&quot;:&quot;Subject&quot;,&quot;title&quot;:&quot;Science&quot;}"
                          data-track-ga="{&quot;category&quot;:&quot;nav_click&quot;,&quot;action&quot;:&quot;subject&quot;,&quot;label&quot;:&quot;Science&quot;}"
                          data-name="NAV_SUBSECTION_PARENT"
                          data-detail="{&quot;childListId&quot;:&quot;subject-science&quot;}">
                          <span>Science</span>
                          <span class="main-nav-dropdown__item-icon icon-chevron-right-charcoal icon-small"></span>
                        </a>
                      </li>
                      <li class="main-nav-dropdown__item">
                        <a class="main-nav-dropdown__item-control color-charcoal" href="/subject/education"
                          data-track-click="nav_click"
                          data-track-props="{&quot;type&quot;:&quot;Subject&quot;,&quot;title&quot;:&quot;Education &amp; Teaching&quot;}"
                          data-track-ga="{&quot;category&quot;:&quot;nav_click&quot;,&quot;action&quot;:&quot;subject&quot;,&quot;label&quot;:&quot;Education &amp; Teaching&quot;}"
                          data-name="NAV_SUBSECTION_PARENT"
                          data-detail="{&quot;childListId&quot;:&quot;subject-education&quot;}">
                          <span>Education &amp; Teaching</span>
                          <span class="main-nav-dropdown__item-icon icon-chevron-right-charcoal icon-small"></span>
                        </a>
                      </li>
                      <li class="main-nav-dropdown__item">
                        <a class="main-nav-dropdown__item-control color-charcoal" href="/subject/social-sciences"
                          data-track-click="nav_click"
                          data-track-props="{&quot;type&quot;:&quot;Subject&quot;,&quot;title&quot;:&quot;Social Sciences&quot;}"
                          data-track-ga="{&quot;category&quot;:&quot;nav_click&quot;,&quot;action&quot;:&quot;subject&quot;,&quot;label&quot;:&quot;Social Sciences&quot;}"
                          data-name="NAV_SUBSECTION_PARENT"
                          data-detail="{&quot;childListId&quot;:&quot;subject-social-sciences&quot;}">
                          <span>Social Sciences</span>
                          <span class="main-nav-dropdown__item-icon icon-chevron-right-charcoal icon-small"></span>
                        </a>
                      </li>
                      <li class="main-nav-dropdown__item">
                        <a class="main-nav-dropdown__item-control color-charcoal" href="/subject/art-and-design"
                          data-track-click="nav_click"
                          data-track-props="{&quot;type&quot;:&quot;Subject&quot;,&quot;title&quot;:&quot;Art &amp; Design&quot;}"
                          data-track-ga="{&quot;category&quot;:&quot;nav_click&quot;,&quot;action&quot;:&quot;subject&quot;,&quot;label&quot;:&quot;Art &amp; Design&quot;}"
                          data-name="NAV_SUBSECTION_PARENT"
                          data-detail="{&quot;childListId&quot;:&quot;subject-art-and-design&quot;}">
                          <span>Art &amp; Design</span>
                          <span class="main-nav-dropdown__item-icon icon-chevron-right-charcoal icon-small"></span>
                        </a>
                      </li>
                      <li class="main-nav-dropdown__item">
                        <a class="main-nav-dropdown__item-control color-charcoal" href="/subject/data-science"
                          data-track-click="nav_click"
                          data-track-props="{&quot;type&quot;:&quot;Subject&quot;,&quot;title&quot;:&quot;Data Science&quot;}"
                          data-track-ga="{&quot;category&quot;:&quot;nav_click&quot;,&quot;action&quot;:&quot;subject&quot;,&quot;label&quot;:&quot;Data Science&quot;}"
                          data-name="NAV_SUBSECTION_PARENT"
                          data-detail="{&quot;childListId&quot;:&quot;subject-data-science&quot;}">
                          <span>Data Science</span>
                          <span class="main-nav-dropdown__item-icon icon-chevron-right-charcoal icon-small"></span>
                        </a>
                      </li>
                      <li class="main-nav-dropdown__item">
                        <a class="main-nav-dropdown__item-control color-charcoal"
                          href="/subject/programming-and-software-development" data-track-click="nav_click"
                          data-track-props="{&quot;type&quot;:&quot;Subject&quot;,&quot;title&quot;:&quot;Programming&quot;}"
                          data-track-ga="{&quot;category&quot;:&quot;nav_click&quot;,&quot;action&quot;:&quot;subject&quot;,&quot;label&quot;:&quot;Programming&quot;}"
                          data-name="NAV_SUBSECTION_PARENT"
                          data-detail="{&quot;childListId&quot;:&quot;subject-programming-and-software-development&quot;}">
                          <span>Programming</span>
                          <span class="main-nav-dropdown__item-icon icon-chevron-right-charcoal icon-small"></span>
                        </a>
                      </li>
                      <li class="main-nav-dropdown__item">
                        <a class="main-nav-dropdown__item-control color-charcoal" href="/subject/personal-development"
                          data-track-click="nav_click"
                          data-track-props="{&quot;type&quot;:&quot;Subject&quot;,&quot;title&quot;:&quot;Personal Development&quot;}"
                          data-track-ga="{&quot;category&quot;:&quot;nav_click&quot;,&quot;action&quot;:&quot;subject&quot;,&quot;label&quot;:&quot;Personal Development&quot;}"
                          data-name="NAV_SUBSECTION_PARENT"
                          data-detail="{&quot;childListId&quot;:&quot;subject-personal-development&quot;}">
                          <span>Personal Development</span>
                          <span class="main-nav-dropdown__item-icon icon-chevron-right-charcoal icon-small"></span>
                        </a>
                      </li>
                      <li class="main-nav-dropdown__item">
                        <a class="main-nav-dropdown__item-control color-charcoal" href="/subject/infosec"
                          data-track-click="nav_click"
                          data-track-props="{&quot;type&quot;:&quot;Subject&quot;,&quot;title&quot;:&quot;Information Security (InfoSec)&quot;}"
                          data-track-ga="{&quot;category&quot;:&quot;nav_click&quot;,&quot;action&quot;:&quot;subject&quot;,&quot;label&quot;:&quot;Information Security (InfoSec)&quot;}"
                          data-name="NAV_SUBSECTION_PARENT"
                          data-detail="{&quot;childListId&quot;:&quot;subject-infosec&quot;}">
                          <span>Information Security (InfoSec)</span>
                          <span class="main-nav-dropdown__item-icon icon-chevron-right-charcoal icon-small"></span>
                        </a>
                      </li>
                    </ul>'''



soup = bs4.BeautifulSoup(html_doc, 'html.parser')

all_text = []
for element in soup.descendants:
    all_text.append(element.text)

pdb.set_trace()




def create_soup():
    res= requests.get("https://www.classcentral.com/")

    soup = bs4.BeautifulSoup(res.text,'lxml')

    pdb.set_trace()

    return soup