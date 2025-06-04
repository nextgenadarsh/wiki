Collection
---

# IEnumerable

- Provides the basic functionality to iterate through a collection using a foreach loop.
- Supports only-read access.
- Ideal for situations where you only need to iterate through a collection.

# ICollection

- Inherits from IEnumerable.
- Represents a collective group of elements with the addition of functionalities like size, enumeration, and synchronization.
- Adds basic collection manipulation like Add, Remove, and Clear.
- Supports both read and write access.
- Provides properties like Count and IsReadOnly.
- Provides methods like Add, Remove, Clear, and Contains.

# IList

- Inherits from ICollection.
- Represents a list of items that are accessible by index.
- Provides advanced collection manipulation like insert and remove by index.
- Supports random access to elements.
- Contains properties like Item (property to access elements by index) and methods like Insert and RemoveAt.
