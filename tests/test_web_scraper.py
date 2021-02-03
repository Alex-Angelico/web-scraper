from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report


def test_citation_count():
    actual = get_citations_needed_count(
        'https://en.wikipedia.org/wiki/2020_Nagorno-Karabakh_war')
    expected = 2
    assert actual == expected


def test_citation_report():
    actual = get_citations_needed_report(
        'https://en.wikipedia.org/wiki/2020_Nagorno-Karabakh_war')
    expected = 'The accounts of engagements in this conflict rely primarily on official statements from belligerents.[citation needed] The engagements have been characterized by the use of armoured warfare; drone warfare,[160] especially the use of Turkish-made Bayraktar TB2 and Israeli loitering munition Harop drones;[94][92] heavy artillery; rocket attacks; and trench warfare.[161] Throughout the campaign, Azerbaijan has relied heavily on drones to strike at Armenian/Artsakh forces, and managed to inflict heavy losses. Having successfully targeted tanks, artillery, and air defense systems, Azerbaijani drones also began targeting units of soldiers. However, some Azerbaijani drones were shot down.[162][163] It has also featured the deployment of cluster munitions, which are banned by the majority of the international community but not by Armenia or Azerbaijan:[164] international third parties have confirmed that Armenia had deployed cluster munitions on civilian-populated areas outside of the conflict zone,[165] and international third parties have confirmed evidence of Azerbaijan\'s use of cluster munitions against civilian areas of Nagorno-Karabakh.[166][167] A series of attacks have inflicted mass civilian casualties in Ganja, Azerbaijan, while civilian residences and infrastructure in Stepanakert, Artsakh\'s capital, and elsewhere have been targeted, inflicting casualties and causing extensive damage.[168] Disinformation and misinformation have accompanied the conflict.[169]\n\nAfter the shelling of Khojavend (Martuni),[178] Artsakh authorities began mobilizing civilians.[179] Just before 04:00 (00:00 UTC) on 10 October 2020, Russia reported that both Armenia and Azerbaijan had agreed on a humanitarian ceasefire after ten hours of talks in Moscow (the Moscow Statement) and announced that both would enter "substantive" talks.[citation needed] After the declared ceasefire, the President of Artsakh admitted Azerbaijan had been able to achieve some success, moving the front deep into Artsakh territory;[180] the Armenian Prime Minister announced that Armenian forces had conducted a "partial retreat".[181]'
    assert actual == expected
