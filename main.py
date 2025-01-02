import textwrap

from app.mcq_question_generation import MCQGenerator
import nltk
nltk.download('punkt_tab')

def show_result(generated: str, answer: str, context:str, original_question: str = ''):
    
    print('Context:')

    for wrap in textwrap.wrap(context, width=120):
        print(wrap)
    print()

    print('Question:')
    print(generated)

    print('Answer:')
    print(answer)
    print('-----------------------------')


MCQ_Generator = MCQGenerator(True)

context = '''The koala or, inaccurately, koala bear[a] (Phascolarctos cinereus), is an arboreal herbivorous marsupial native to Australia. It is the only extant representative of the family Phascolarctidae and its closest living relatives are the wombats, which are members of the family Vombatidae. The koala is found in coastal areas of the mainland's eastern and southern regions, inhabiting Queensland, New South Wales, Victoria, and South Australia. It is easily recognisable by its stout, tailless body and large head with round, fluffy ears and large, spoon-shaped nose. The koala has a body length of 60–85 cm (24–33 in) and weighs 4–15 kg (9–33 lb). Fur colour ranges from silver grey to chocolate brown. Koalas from the northern populations are typically smaller and lighter in colour than their counterparts further south. These populations possibly are separate subspecies, but this is disputed.'''

context_oxygen = '''Oxygen is the chemical element with the symbol O and atomic number 8. It is a member of the chalcogen group in the periodic table, a highly reactive nonmetal, and an oxidizing agent that readily forms oxides with most elements as well as with other compounds. Oxygen is Earth's most abundant element, and after hydrogen and helium, it is the third-most abundant element in the universe. At standard temperature and pressure, two atoms of the element bind to form dioxygen, a colorless and odorless diatomic gas with the formula O
2. Diatomic oxygen gas currently constitutes 20.95% of the Earth's atmosphere, though this has changed considerably over long periods of time. Oxygen makes up almost half of the Earth's crust in the form of oxides.[3]

Dioxygen provides the energy released in combustion[4] and aerobic cellular respiration,[5] and many major classes of organic molecules in living organisms contain oxygen atoms, such as proteins, nucleic acids, carbohydrates, and fats, as do the major constituent inorganic compounds of animal shells, teeth, and bone. Most of the mass of living organisms is oxygen as a component of water, the major constituent of lifeforms. Oxygen is continuously replenished in Earth's atmosphere by photosynthesis, which uses the energy of sunlight to produce oxygen from water and carbon dioxide. Oxygen is too chemically reactive to remain a free element in air without being continuously replenished by the photosynthetic action of living organisms. Another form (allotrope) of oxygen, ozone (O
3), strongly absorbs ultraviolet UVB radiation and the high-altitude ozone layer helps protect the biosphere from ultraviolet radiation. However, ozone present at the surface is a byproduct of smog and thus a pollutant.

Oxygen was isolated by Michael Sendivogius before 1604, but it is commonly believed that the element was discovered independently by Carl Wilhelm Scheele, in Uppsala, in 1773 or earlier, and Joseph Priestley in Wiltshire, in 1774. Priority is often given for Priestley because his work was published first. Priestley, however, called oxygen "dephlogisticated air", and did not recognize it as a chemical element. The name oxygen was coined in 1777 by Antoine Lavoisier, who first recognized oxygen as a chemical element and correctly characterized the role it plays in combustion.

Common uses of oxygen include production of steel, plastics and textiles, brazing, welding and cutting of steels and other metals, rocket propellant, oxygen therapy, and life support systems in aircraft, submarines, spaceflight and diving.'''

context2 = '''Random Access Memory (RAM) is a critical component in operating systems (OS), acting as the primary volatile memory that temporarily holds data and instructions the CPU needs to execute tasks. Its high-speed nature makes it essential for bridging the performance gap between the processor and slower storage devices like hard drives or SSDs. RAM is organized into a hierarchy of memory segments, such as stack, heap, and memory-mapped regions, each serving specific purposes. The OS employs sophisticated memory management techniques, including paging, segmentation, and virtual memory, to maximize the utilization of RAM. Paging allows the OS to divide programs into fixed-size blocks called pages, which are loaded into frames in physical memory as needed, enabling efficient multitasking and isolation of processes. Virtual memory extends the apparent size of RAM by using disk space as a temporary storage medium for less frequently accessed data, managed by a paging file or swap space. This mechanism is pivotal in handling scenarios where the demand for memory exceeds the physical capacity of RAM, but it can lead to slower performance due to the latency of disk access, known as thrashing. Modern operating systems also leverage features like demand paging, lazy loading, and memory caching to optimize performance. They prioritize frequently accessed data using techniques like the least recently used (LRU) algorithm to determine what remains in memory. Additionally, OS-level memory protection mechanisms ensure process isolation, preventing unauthorized access to memory segments, thereby enhancing system stability and security. Innovations like Non-Uniform Memory Access (NUMA) and memory compression in contemporary systems further optimize RAM utilization, particularly in multi-core and high-performance computing environments. Understanding and managing RAM effectively is essential for achieving an optimal balance between performance, resource allocation, and system reliability in operating systems.'''

MCQ_Generator.generate_mcq_questions(context2, 10) 
